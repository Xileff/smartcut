from flask import Blueprint, request, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.IdCardsService import *

id_card_route = Blueprint("id_card_route", __name__)


@id_card_route.route("/identities", methods=["POST"])
@jwt_required()
def post_id_card_handler():
    picture = request.files.get("picture")
    national_id = request.form.get("nationalId")
    user_id = get_jwt_identity()

    add_id_card(national_id, picture, user_id)

    return make_response(
        {"status": "success", "message": "Your identity card will be verified shortly"},
        201,
    )
