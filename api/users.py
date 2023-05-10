from flask import Blueprint, request, make_response
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity
from services.UsersService import *

user_route = Blueprint("user_route", __name__)


@user_route.route("/users", methods=["POST"])
def add_user_handler():
    data = request.get_json()
    id = add_user(data)
    return make_response(
        {
            "status": "success",
            "message": "Berhasil didaftarkan",
            "data": {
                "userId": id,
            },
        },
        201,
    )


@user_route.route("/users/login", methods=["POST"])
def login_user_handler():
    data = request.get_json()
    token = login(data)
    return make_response(
        {
            "status": "success",
            "message": "Berhasil login",
            "data": {"token": token},
        },
        200,
    )


@user_route.route("/users/<string:id>/edit", methods=["PUT"])
@jwt_required()
def edit_user_handler(id):
    jwt_user_id = get_jwt_identity()
    if jwt_user_id != id:
        return make_response({"status": "fail", "message": "Unauthorized access"}, 401)

    # data = request.get_json() # todo edit profile

    return make_response(
        {"status": "success", "message": "Berhasil mengedit data"},
        200,
    )
