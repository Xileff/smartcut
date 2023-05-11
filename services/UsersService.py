from nanoid import generate
from models.User import User
from sqlalchemy import or_
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import BadRequest, Unauthorized, Conflict
from flask_jwt_extended import create_access_token
import datetime
from datetime import timedelta


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

    raise Unauthorized("Gagal login. Username atau password salah")


def get_profile_by_id(id: str):
    user = User.query.filter_by(id=id).first()
    return user.serialize()


def edit_profile_by_id(id: str, data: dict):
    name, email, phone = data.values()

    if any([name == "", email == "", phone == ""]):
        raise BadRequest("Name, email, and phone are required")

    user = User.query.filter_by(id=id).first()
    user.name = name
    user.email = email
    user.phone = phone

    user.save()
