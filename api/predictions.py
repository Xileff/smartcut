from flask import Blueprint, request, make_response
from services.PredictionsService import *

predictions_route = Blueprint("predictions_route", __name__)
