from app import db

class UserCalculation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    distance = db.Column(db.Float, nullable=False)
    fuel_efficiency = db.Column(db.Float, nullable=False)
    carbon_footprint = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<UserCalculation {self.id}>'
