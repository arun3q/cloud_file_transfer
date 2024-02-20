import os
import boto3
from google.cloud import storage
from .config import FILE_TYPES_TO_S3, FILE_TYPES_TO_GCS

def upload_files(directory):
    s3_client = boto3.client('s3')
    gcs_client = storage.Client()

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            if any(file.endswith(ext) for ext in FILE_TYPES_TO_S3):
                upload_to_s3(s3_client, file_path)

            elif any(file.endswith(ext) for ext in FILE_TYPES_TO_GCS):
                upload_to_gcs(gcs_client, file_path)

def upload_to_s3(client, file_path, bucket_name='s3-bucket'):
    client.upload_file(file_path, bucket_name, os.path.basename(file_path))
    print(f"Uploaded {file_path} to S3 bucket {bucket_name}")

def upload_to_gcs(client, file_path, bucket_name='gcs-bucket'):
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(os.path.basename(file_path))
    blob.upload_from_filename(file_path)
    print(f"Uploaded {file_path} to GCS bucket {bucket_name}")
