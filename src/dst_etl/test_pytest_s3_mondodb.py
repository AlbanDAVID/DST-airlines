import pytest
from botocore.client import ClientError
import boto3
import certifi
from pymongo import MongoClient

def aws_S3_connection():
    s3_client = boto3.client('s3', aws_access_key_id='AKIAUBEGQUNAZW3YUCNW' , aws_secret_access_key='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')

    try:
        s3_client.head_bucket(Bucket="datalake-airlines")
        connection = "Successful connection"
    except ClientError:
        connection = "Failed connection"
        
    return connection

def aws_mongodb_connection():
    try:
        ca = certifi.where()
        client = MongoClient("mongodb+srv://user01:wpvPnKP2gdPW8inB@cluster0.tyo5f.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
        db = client.data_airlines
        client.server_info()
        connection = "Successful connection"
    except ClientError:
            connection = "Failed connection"
            
    return connection

def test_aws_S3_connection():
    assert aws_S3_connection() == "Successful connection"


def test_aws_mongodb_connection():
    assert aws_mongodb_connection() == 'Successful connection'
