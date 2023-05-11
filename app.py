from flask import Flask, make_response, Response
from flask_cors import CORS
from flask_migrate import Migrate
from werkzeug.exceptions import HTTPException
import logging
from utils.config import Config
from utils.database import db
from utils.tokenize import jwt
from api.users import user_route

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
jwt.init_app(app)
migrate = Migrate(app, db)

CORS(app)

app.register_blueprint(user_route)


@app.errorhandler(HTTPException)
def handle_http_exception(e: HTTPException):
    return make_response({"status": "fail", "message": e.description}, e.code)


@app.errorhandler(Exception)
def handle_server_error(e: Exception):
    logging.error(str(e), exc_info=True)
    return make_response(
        {"status": "fail", "message": "Oops, sorry. Something went wrong on our side."},
        500,
    )


logging.basicConfig(level=logging.ERROR)


@app.after_request
def add_header(response: Response):
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
