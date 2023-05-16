from nanoid import generate
from models.User import User
from sqlalchemy import or_
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import BadRequest, Unauthorized, Conflict, NotFound
from flask_jwt_extended import create_access_token
import datetime
from datetime import timedelta
from utils.storage import bucket
from utils.config import Config


def add_user(data: dict):
    required_keys = ["name", "username", "password", "email", "phone"]

    if not all(key in data for key in required_keys):
        raise BadRequest(
            "Gagal menambahkan user. Mohon lengkapi nama, username, password, email dan nomor telepon"
        )

    name, username, password, email, phone = data.values()

    existing_user = User.query.filter(
        or_(User.username == username, User.email == email, User.phone == phone)
    ).first()

    if existing_user:
        raise Conflict(
            "Gagal menambahkan user. Username, email, atau nomor telepon sudah dipakai."
        )

    id = "user-" + generate(size=16)
    dateJoined = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    user = User(
        id=id,
        name=name,
        username=username,
        password=generate_password_hash(password),
        email=email,
        phone=phone,
        date_joined=dateJoined,
        is_email_verified=False,
        is_barber=False,
    )

    user.save()
    return id


def login(data: dict):
    username, password = data.values()
    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        return create_access_token(
            identity=user.id, expires_delta=timedelta(minutes=30)
        )

    raise Unauthorized("Wrong password or username")


def get_profile_by_id(id: str):
    user = User.query.filter_by(id=id).first()
    return user.serialize()


def edit_profile_by_id(id: str, data: dict):
    name, email, phone = data.values()

    if any([name == "", email == "", phone == ""]):
        raise BadRequest("Name, email, and phone are required")

    user = User.query.filter_by(id=id).first()

    if not user:
        raise NotFound("User not found")

    user.name = name
    user.email = email
    user.phone = phone

    user.save()


def upload_profile_picture_by_id(id, picture):
    user: User = User.query.filter_by(id=id).first()
    if not user:
        raise NotFound("User not found")

    picture_ext = picture.filename.split(".")[-1]
    if picture_ext not in ["jpg", "jpeg", "png"]:
        raise BadRequest("Image format must be jpg or jpeg or png")

    storage_path = Config.USER_PROFILE_PICTURE_PATH
    if user.picture:
        previous_picture_name = user.picture.split("/")[-1]
        storage_reference = bucket.blob(storage_path + previous_picture_name)
        storage_reference.delete()

    picture.filename = user.id + "." + picture_ext
    storage_reference = bucket.blob(storage_path + picture.filename)
    storage_reference.upload_from_file(picture, content_type="image")
    public_url = storage_reference.public_url

    user.picture = public_url
    user.save()

    return public_url


def remove_profile_picture_by_id(id):
    user = User.query.filter_by(id=id).first()
    if not user:
        raise NotFound("User not found")

    storage_path = Config.USER_PROFILE_PICTURE_PATH
    if not user.picture:
        raise NotFound("This user has no profile picture to be deleted")

    previous_picture_name = user.picture.split("/")[-1]
    storage_reference = bucket.blob(storage_path + previous_picture_name)
    storage_reference.delete()

    user.picture = None
    user.save()
