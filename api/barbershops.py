from flask import Blueprint, request, make_response
from services.BarbershopsService import *

barbershop_route = Blueprint("barbershop_route", __name__)
