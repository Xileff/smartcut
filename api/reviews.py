from flask import Blueprint, request, make_response
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import BadRequest
from utils.tokenize import verify_user_identity
from services.ReviewsService import *

review_route = Blueprint("reviews_route", __name__)


@review_route.route("/reviews", methods=["POST"])
@jwt_required()
def post_review_handler():
    data = request.json

    if not data["userId"]:
        raise BadRequest("User id is required")

    user_id = data["userId"]
    verify_user_identity(user_id)

    message = add_review(data)

    return make_response(
        {
            "status": "success",
            "message": message,
        }
    )
