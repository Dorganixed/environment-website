from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import UserCalculation, db
from .calculator import calculate_carbon_footprint

calculator_blueprint = Blueprint('calculator', __name__)

@calculator_blueprint.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        distance = float(request.form['distance'])
        fuel_efficiency = float(request.form['fuel_efficiency'])
        carbon_footprint = calculate_carbon_footprint(distance, fuel_efficiency)

        new_calculation = UserCalculation(
            distance=distance,
            fuel_efficiency=fuel_efficiency,
            carbon_footprint=carbon_footprint
        )

        db.session.add(new_calculation)
        db.session.commit()

        flash('Calculation saved successfully!')
        return redirect(url_for('calculator.calculate'))

    return render_template('calculate.html')

@calculator_blueprint.route('/calculations')
def view_calculations():
    calculations = UserCalculation.query.all()
    return render_template('calculations.html', calculations=calculations)
