from flask import Blueprint, request, make_response
from services.AppointmentsService import *

appointment_route = Blueprint("appointment_route", __name__)
