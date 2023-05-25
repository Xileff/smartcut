from models.Appointment import Appointment
from models.Barbershop import Barbershop
from werkzeug.exceptions import BadRequest, Unauthorized
from nanoid import generate


def add_appointment(data, user_id):
    required_keys = ["schedule", "message", "barbershopId"]

    if not all(key in data for key in required_keys):
        raise BadRequest("Schedule, message, and barbershop id must be filled")

    schedule = data["schedule"]
    message = data["message"]
    barbershop_id = data["barbershopId"]

    if any([schedule == "", barbershop_id == ""]):
        raise BadRequest("Invalid schedule or barbershop")

    user_has_barbershop = Barbershop.query.filter_by(user_id=user_id).first()
    if user_has_barbershop and user_has_barbershop.id == barbershop_id:
        raise BadRequest(
            "Why would you book an appointment in your own barbershop? It does not make sense, my man."
        )

    app_id = "app-" + generate(size=16)

    appointment = Appointment(
        id=app_id,
        schedule=schedule,
        message=message,
        is_finished=False,
        is_canceled=False,
        will_be_canceled=False,
        date_canceled=None,
        barbershop_id=barbershop_id,
        user_id=user_id,
    )

    appointment.save()

    return app_id


def get_appointments(user_id):
    appointments = Appointment.query.filter_by(user_id=user_id).all()
    return [appointment.serialize() for appointment in appointments]


def get_appointment(id):
    appointment = Appointment.query.filter_by(id=id).first()
    return appointment.serialize()


def finish_appointment(id, data, user_id):
    if not data["action"]:
        raise BadRequest("Invalid request, action type is required : finish or cancel?")

    action = data["action"]

    appointment = Appointment.query.filter_by(id=id).first()

    if appointment.user_id != user_id:
        raise Unauthorized("Unauthorized access")

    if action == "finish":
        appointment.is_finished = True
        message = "Appointment " + appointment.id + " finished"
    elif action == "cancel":
        appointment.will_be_canceled = True
        message = "Appointment " + appointment.id + " canceled"

    appointment.save()
    return message
