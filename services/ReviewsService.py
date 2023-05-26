from werkzeug.exceptions import BadRequest, NotFound
from nanoid import generate
from models.Review import Review
from models.Appointment import Appointment


def add_review(data):
    required_keys = ["stars", "message", "appointmentId"]
    if not all([key in data for key in required_keys]):
        raise BadRequest("All fields are required")

    stars = data["stars"]
    message = data["message"]
    appointment_id = data["appointmentId"]

    appointment = Appointment.query.filter_by(id=appointment_id).first()

    if not appointment:
        raise NotFound("Invalid appointment id")

    if not appointment.is_finished:
        raise BadRequest("This appointment is not finished yet")

    review_id = generate(size=16)
    review = Review(
        id=review_id,
        stars=stars,
        message=message,
        appointment_id=appointment_id,
    )

    review.save()

    message = appointment_id + " reviewed succesfully"
    return message
