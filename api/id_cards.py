from flask import Blueprint, request, make_response
from services.IdCardsService import *

id_card_route = Blueprint("id_card_route", __name__)
