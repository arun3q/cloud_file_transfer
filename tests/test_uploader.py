import pytest
from moto import mock_s3
import boto3
from file_transfer.uploader import upload_to_s3
import os

@pytest.fixture
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_SECURITY_TOKEN'] = 'testing'
    os.environ['AWS_SESSION_TOKEN'] = 'testing'

@pytest.fixture
def s3(aws_credentials):
    with mock_s3():
        yield boto3.client('s3', region_name='us-east-1')

def test_upload_to_s3(s3):
    bucket_name = 'test-bucket'
    s3.create_bucket(Bucket=bucket_name)
    upload_to_s3(s3, 'test.txt', bucket_name=bucket_name)
    response = s3.list_objects_v2(Bucket=bucket_name)
    assert 'Contents' in response
    assert response['Contents'][0]['Key'] == 'test.txt'
