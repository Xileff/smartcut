import os
from google.cloud import storage

client = storage.Client.from_service_account_json(os.getenv("STORAGE_KEY"))
bucket = client.get_bucket(os.getenv("STORAGE_BUCKET"))
