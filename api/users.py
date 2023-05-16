from flask import Blueprint, request, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.exceptions import Forbidden
from services.UsersService import *
from utils.tokenize import verify_user_identity

user_route = Blueprint("user_route", __name__)


@user_route.route("/users", methods=["POST"])
def post_user_handler():
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
def post_user_login_handler():
    data = request.get_json()
    token = login(data)
    return make_response(
        {
            "status": "success",
            "message": "Berhasil login",
            "data": {"token": token},
        },
    )


@user_route.route("/users/<string:id>", methods=["PUT"])
@jwt_required()
def put_user_by_id_handler(id):
    verify_user_identity(id)
    data = request.get_json()
    edit_profile_by_id(id, data)

    return make_response({"status": "success", "message": "Berhasil mengedit data"})


@user_route.route("/users/<string:username>", methods=["GET"])
@jwt_required()
def get_user_by_id_handler(username):
    user = get_profile_by_username(username)
    return make_response({"status": "success", "data": {"user": user}})


@user_route.route("/users/<string:id>/profile-picture", methods=["PUT"])
@jwt_required()
def put_user_profile_picture_by_id_handler(id):
    verify_user_identity(id)
    picture = request.files["picture"]
    picture_url = upload_profile_picture_by_id(id, picture)
    return make_response(
        {
            "status": "success",
            "message": "Profile picture uploaded succesfully.",
            "data": {"picture_url": picture_url},
        }
    )


@user_route.route("/users/<string:id>/profile-picture", methods=["DELETE"])
@jwt_required()
def delete_user_profile_picture_by_id_handler(id):
    verify_user_identity(id)
    remove_profile_picture_by_id(id)
    return make_response({"status": "success", "message": "Profile picture removed"})
