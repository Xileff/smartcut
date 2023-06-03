from flask import Blueprint, request, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.AppointmentsService import *
from utils.tokenize import verify_user_identity

appointment_route = Blueprint("appointment_route", __name__)


@appointment_route.route("/appointments/<string:uid>", methods=["POST"])
@jwt_required()
def post_appointment_handler(uid):
    verify_user_identity(uid)

    data = request.json
    appointment_id = add_appointment(data, uid)

    return make_response(
        {
            "status": "success",
            "data": {
                "appointmentId": appointment_id,
            },
        },
        201,
    )


@appointment_route.route("/appointments", methods=["GET"])
@jwt_required()
def get_appointments_handler():
    user_id = get_jwt_identity()
    appointments = get_appointments(user_id)
    return make_response(
        {
            "status": "success",
            "data": {
                "appointments": appointments,
            },
        }
    )


@appointment_route.route("/appointments/<string:id>", methods=["GET"])
@jwt_required()
def get_appointment_by_id_handler(id):
    appointment = get_appointment(id)
    return make_response(
        {
            "status": "success",
            "data": appointment,
        }
    )


@appointment_route.route("/appointments/<string:id>", methods=["PUT"])
@jwt_required()
def finish_appointment_by_id_handler(id):
    data = request.json
    user_id = get_jwt_identity()

    message = finish_appointment(id, data, user_id)

    return make_response({"status": "success", "message": message})
