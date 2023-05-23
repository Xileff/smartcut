from flask import Blueprint, request, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.BarbershopsService import *
from utils.tokenize import verify_user_identity

barbershop_route = Blueprint("barbershop_route", __name__)


@barbershop_route.route("/barbershops", methods=["POST"])
@jwt_required()
def post_barbershop_handler():
    data = {
        "name": request.form.get("name"),
        "address": request.form.get("address"),
        "picture": request.files.get("picture"),
        "latitude": request.form.get("latitude"),
        "longitude": request.form.get("longitude"),
        "user_id": get_jwt_identity(),
    }

    add_barbershop(data)

    return make_response({"status": "success", "message": "Barbershop created!"})


@barbershop_route.route("/barbershops/<string:uid>", methods=["PUT"])
@jwt_required()
def put_barbershop_handler(uid):
    verify_user_identity(uid)
    data = {
        "name": request.form.get("name"),
        "address": request.form.get("address"),
        "picture": request.files.get("picture"),
        "latitude": request.form.get("latitude"),
        "longitude": request.form.get("longitude"),
    }
    edit_barbershop(uid, data)

    return make_response({"status": "success", "message": "Barbershop edited"})


@barbershop_route.route("/barbershops", methods=["GET"])
def get_barbershops_handler():
    return


@barbershop_route.route("/barbershops/<string:id>", methods=["GET"])
def get_barbershop_by_id_handler(id):
    return
