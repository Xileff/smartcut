from nanoid import generate
from models.User import User
from sqlalchemy import or_
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import BadRequest, Unauthorized, Conflict, NotFound
from flask_jwt_extended import create_access_token
import datetime
from datetime import timedelta
from utils.config import Config
from utils.storage import upload_picture, remove_file


def add_user(data: dict):
    required_keys = ["name", "username", "password", "email", "phone"]

    if not all(key in data for key in required_keys):
        raise BadRequest(
            "Registration failed. All fields(name, username, password, email, phone) are required."
        )

    name, username, password, email, phone = data.values()

    existing_user = User.query.filter(
        or_(User.username == username, User.email == email, User.phone == phone)
    ).first()

    if existing_user:
        raise Conflict(
            "Registration failed. Either username, email, or phone number has already been used to register."
        )

    id = "user-" + generate(size=16)
    dateJoined = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    user = User(
        id=id,
        name=name,
        username=username,
        password=generate_password_hash(password),
        email=email,
        phone="62" + phone[1:] if phone.startswith("0") else phone,
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


def get_profile_by_username(username: str):
    user = User.query.filter_by(username=username).first()
    if not user:
        raise NotFound("User not found")
    return user.serialize()


def edit_profile_by_id(id: str, data: dict):
    name, email, phone = data.values()

    if any([name == "", email == "", phone == ""]):
        raise BadRequest("Name, email, and phone are required")

    user = User.query.filter_by(id=id).first()

    if not user:
        raise NotFound("User not found")

    user.name = name
    user.phone = phone
    if user.email != email:
        user.email = email
        user.is_email_verified = False

    user.save()


def upload_profile_picture_by_id(id, picture):
    user: User = User.query.filter_by(id=id).first()

    if not user:
        raise NotFound("User not found")

    if user.picture:
        previous_picture_name = user.picture.split("/")[-1]
        remove_file(Config.USER_PROFILE_PICTURE_PATH, previous_picture_name)

    public_url = upload_picture(
        picture=picture, path=Config.USER_PROFILE_PICTURE_PATH, filename=user.id
    )

    user.picture = public_url
    user.save()

    return public_url


def remove_profile_picture_by_id(id):
    user = User.query.filter_by(id=id).first()

    if not user:
        raise NotFound("User not found")

    if not user.picture:
        raise NotFound("This user has no profile picture to be deleted")

    picture_name = user.picture.split("/")[-1]
    remove_file(path=Config.USER_PROFILE_PICTURE_PATH, filename=picture_name)

    user.picture = None
    user.save()
