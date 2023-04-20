import base64
from azure.storage.blob import BlobServiceClient
from config import extract_connection_string, extract_container_name, load_connection_string, load_container_name

def execute():
    files: dict = extract()
    transformed_files: dict = transform(files)
    load(transformed_files)


def extract() -> dict:
    storage_account = BlobServiceClient.from_connection_string(extract_connection_string)
    container = storage_account.get_container_client(extract_container_name)
    files: dict = {}
    for blob in container.list_blobs():
        b = container.get_blob_client(blob.name)
        files[blob.name] = b.download_blob().readall()
    return files


def transform(files: dict) -> dict:
    return {key: base64.b64decode(value + b'==').decode('utf8') for key, value in files.items()}


def load(files: dict):
    storage_account = BlobServiceClient.from_connection_string(load_connection_string)
    for key in files:
        blob_client = storage_account.get_blob_client(container=load_container_name, blob=key)
        blob_client.upload_blob(files[key])