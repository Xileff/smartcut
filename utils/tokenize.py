from flask_jwt_extended import JWTManager, get_jwt_identity
from werkzeug.exceptions import Forbidden

jwt = JWTManager()


def verify_user_identity(uid):
    id = get_jwt_identity()
    if uid != id:
        raise Forbidden("Unauthorized access")
