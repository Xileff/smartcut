from nanoid import generate
from models.User import User
from sqlalchemy import or_
from exceptions.Client import ClientError
import datetime


def add_user(data: dict):
    required_keys = ["name", "username", "password", "email", "phone"]

    if not all(key in data for key in required_keys):
        raise ClientError(
            "Gagal menambahkan user. Mohon lengkapi nama, username, password, email dan nomor telepon",
            400,
        )

    name, username, password, email, phone = data.values()

    existing_user = User.query.filter(
        or_(User.username == username, User.email == email, User.phone == phone)
    ).first()

    if existing_user:
        raise ClientError(
            "Gagal menambahkan user. Username, email, atau nomor telepon sudah dipakai.",
            409,
        )

    id = generate(size=16)
    dateJoined = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    user = User(
        id=id,
        name=name,
        username=username,
        password=password,
        email=email,
        phone=phone,
        date_joined=dateJoined,
    )

    user.save()
    return id


def add_profile_picture():
    return
