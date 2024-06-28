from flask import Blueprint

calculator_blueprint = Blueprint('calculator', __name__)

from . import views, models
