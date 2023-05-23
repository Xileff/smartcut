from models.IdCard import IdCard
from models.User import User
from werkzeug.exceptions import BadRequest, Conflict, NotFound
from utils.storage import upload_picture
from utils.config import Config


def add_id_card(national_id, picture, user_id):
    if len(str(national_id)) != 16:
        raise BadRequest("National ID(NIK) not valid")

    user = User.query.filter_by(id=user_id).first()
    if not user:
        raise NotFound("User not found")

    existing_id_card = IdCard.query.filter_by(user_id=user_id).first()
    if existing_id_card:
        raise Conflict("This user already already has an id card")

    if not picture:
        raise BadRequest("Id card picture is mandatory")

    public_url = upload_picture(
        picture=picture, path=Config.ID_CARD_PICTURE_PATH, filename=user.id
    )

    id_card = IdCard(
        id=national_id,
        picture=public_url,
        user_id=user.id,
    )

    id_card.save()
