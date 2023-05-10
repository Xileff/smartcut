# todo dotenv
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = (
        "mysql://"
        + os.getenv("DB_USER")
        + ":"
        + os.getenv("DB_PASSWORD")
        + "@"
        + os.getenv("DB_HOST")
        + "/"
        + os.getenv("DB_NAME")
    )

    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
