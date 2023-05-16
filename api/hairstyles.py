from flask import Blueprint, request, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.exceptions import Forbidden
from services.HairstylesService import *

hairstyles_route = Blueprint("hairstyles_route", __name__)


@hairstyles_route.route("/hairstyles", methods=["GET"])
@jwt_required()
def get_hairstyles_handler():
    name = request.args.get("name")
    category = request.args.get("category")
    hairstyles = get_hairstyles(name, category)
    return make_response(
        {
            "status": "success",
            "data": {
                "hairstyles": hairstyles,
            },
        }
    )
