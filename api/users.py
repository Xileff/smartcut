from flask import Blueprint, request, make_response

from services.UsersService import *

user_route = Blueprint("user_route", __name__)


@user_route.route("/users", methods=["POST"])
def add_user_handler():
    data = request.get_json()
    id = add_user(data)
    return make_response(
        {
            "status": "success",
            "message": "User berhasil didaftarkan",
            "data": {
                "userId": id,
            },
        },
        201,
    )
