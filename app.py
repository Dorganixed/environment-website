from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///enviro.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class UserCalculation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    distance = db.Column(db.Float, nullable=False)
    fuel_efficiency = db.Column(db.Float, nullable=False)
    carbon_footprint = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<UserCalculation {self.id}>'

@app.route('/')
def index():
    calculations = UserCalculation.query.all()
    return render_template('index.html', calculations=calculations)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about/carbon-footprint')
def about_carbon_footprint():
    return render_template('about_carbon_footprint.html')

@app.route('/reduce')
def reduce():
    return render_template('reduce.html')

@app.route('/studies')
def global_efforts():
    return render_template('studies.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        flash('Your message has been sent successfully!')
        return redirect(url_for('contact'))

    return render_template('contact.html')

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        distance = float(request.form['distance'])
        fuel_efficiency = float(request.form['fuel_efficiency'])
        carbon_footprint = distance / fuel_efficiency * 2.31  # Example calculation

        new_calculation = UserCalculation(
            distance=distance,
            fuel_efficiency=fuel_efficiency,
            carbon_footprint=carbon_footprint
        )
        db.session.add(new_calculation)
        db.session.commit()

        flash('Calculation saved successfully!')
        return redirect(url_for('index'))

    return render_template('calculate.html')

@app.route('/calculations')
def view_calculations():
    calculations = UserCalculation.query.all()
    return render_template('calculations.html', calculations=calculations)

@app.route('/mission-goals')
def mission_goals():
    return render_template('mission_goals.html')

@app.route('/carbon_footprint_history')
def carbon_footprint_history():
    return render_template('carbon_footprint_history.html')

if __name__ == '__main__':
    app.run(debug=True)
