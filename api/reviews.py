from flask import Blueprint, request, Response
from services.ReviewsService import *

review_route = Blueprint("reviews_route", __name__)
