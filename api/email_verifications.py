from flask import Blueprint, request, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.exceptions import Forbidden
from services.EmailVerificationsService import *

verification_route = Blueprint("verification_route", __name__)


@verification_route.route("/verifications/<string:user_id>", methods=["POST"])
@jwt_required()
def post_verifications_handler(user_id):
    id = get_jwt_identity()
    if id != user_id:
        raise Forbidden("Unauthorized access")

    create_verification_code(user_id=user_id)

    return make_response(
        {
            "status": "success",
            "message": "Please check your email for verification code",
        }
    )
