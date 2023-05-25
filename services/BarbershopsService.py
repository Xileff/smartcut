# BarbershopsService.py

from models.Barbershop import Barbershop
from models.IdCard import IdCard
from models.User import User
from werkzeug.exceptions import BadRequest, NotFound, Forbidden, Conflict
from nanoid import generate
from utils.storage import upload_picture, remove_file
from utils.config import Config


def add_barbershop(data):
    required_keys = [
        "name",
        "address",
        "picture",
        "description",
        "latitude",
        "longitude",
        "user_id",
    ]
    name, address, picture, description, latitude, longitude, user_id = data.values()

    barbershop_exists = Barbershop.query.filter_by(user_id=user_id).first()
    if barbershop_exists:
        raise Conflict("You already have a barbershop")

    user_id_card = IdCard.query.filter_by(user_id=user_id).first()
    if not user_id_card:
        raise Forbidden(
            "You are not allowed to create a barbershop because you have not verified your identity yet"
        )

    if not all(key in data for key in required_keys):
        raise BadRequest("All fields are required")

    if any([name == "", address == "", latitude == "", longitude == "", user_id == ""]):
        raise BadRequest("All fields must not be empty")

    id = "barbershop-" + generate(size=16)
    picture_url = upload_picture(picture, Config.BARBERSHOP_PICTURE_PATH, id)

    barbershop = Barbershop(
        id=id,
        name=name,
        address=address,
        picture=picture_url,
        description=description,
        latitude=latitude,
        longitude=longitude,
        user_id=user_id,
    )
    barbershop.save()

    user = User.query.filter_by(id=user_id).first()
    user.is_barber = True
    user.save()

    return id


def edit_barbershop(user_id, data):
    barbershop = Barbershop.query.filter_by(user_id=user_id).first()
    if not barbershop:
        raise NotFound("Barbershop not found")

    name, address, picture, description, latitude, longitude = data.values()

    barbershop.name = name
    barbershop.address = address
    barbershop.description = description
    barbershop.latitude = latitude
    barbershop.longitude = longitude

    if picture:
        previous_picture = barbershop.picture.split("/")[-1]
        remove_file(Config.BARBERSHOP_PICTURE_PATH, previous_picture)
        public_url = upload_picture(
            picture=picture, path=Config.BARBERSHOP_PICTURE_PATH, filename=barbershop.id
        )
        barbershop.picture = public_url

    barbershop.save()


def get_barbershops():
    barbershops = Barbershop.query.all()
    return [barbershop.serialize() for barbershop in barbershops]


def get_barbershop_by_id(id):
    barbershop = Barbershop.query.filter_by(id=id).first()
    return barbershop.serialize_simple()
