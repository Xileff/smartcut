from models.Barbershop import Barbershop
from werkzeug.exceptions import BadRequest, NotFound
from nanoid import generate
from utils.storage import upload_picture
from utils.config import Config


def add_barbershop(data, picture):
    required_keys = ["name", "address", "latitude", "longitude", "user_id"]
    name, address, latitude, longitude, user_id = data.values()

    if not all(key in data for key in required_keys):
        raise BadRequest("All fields are required")

    if any([name == "", address == "", latitude == "", longitude == "", user_id == ""]):
        raise BadRequest("All fields must not be empty")

    id = "barbershop" + generate(size=16)
    picture = upload_picture(picture, Config.BARBERSHOP_PICTURE_PATH, id)

    barbershop = Barbershop(
        id=id,
        name=name,
        address=address,
        picture=picture,
        latitude=latitude,
        longitude=longitude,
        user_id=user_id,
    )
    barbershop.save()
