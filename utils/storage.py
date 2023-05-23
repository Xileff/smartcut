import os
from google.cloud import storage
from werkzeug.exceptions import BadRequest

client = storage.Client.from_service_account_json(os.getenv("STORAGE_KEY"))
bucket = client.get_bucket(os.getenv("STORAGE_BUCKET"))


def upload_picture(picture, path, filename):
    picture_ext = picture.filename.split(".")[-1]
    if picture_ext not in ["jpg", "jpeg", "png"]:
        raise BadRequest("Image format must be jpg or jpeg or png")

    picture_file_name = filename + "." + picture_ext
    storage_reference = bucket.blob(path + picture_file_name)
    storage_reference.upload_from_file(picture, content_type="image")

    return storage_reference.public_url
