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
    
@hairstyles_route.route("/hairstyles/<string:id>", methods=["GET"])
@jwt_required()
def get_single_hairstyle_handler(id):
    name = request.args.get("name")
    description = request.args.get("description")
    category = request.args.get("category")
    hairstyle = get_hairstyle_by_id(id)

    if hairstyle is None:
        return make_response(
            {"status": "fail", "message": "Hairstyle not found"}, 404
        )

    response = {
        "status": "success",
        "data": {
            "id": hairstyle["id"],
            "name": hairstyle["name"],
            "description": hairstyle["description"],
            "category": hairstyle["category"],
        },
    }

    return make_response(response, 200)