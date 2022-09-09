import pytest

from botocore.client import ClientError
import boto3
import certifi
from pymongo import MongoClient


def aws_S3_connection_test():
    
    try:
        s3_client = boto3.client('s3', aws_access_key_id='AKIAUBEGQUNAZW3YUCNW',aws_secret_access_key='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')
        response = s3_client.list_objects_v2(Bucket='datalake-airlines', Prefix='01-real-time-flights-airlabs/')
        connection = "Successful connection"
    except :
        connection = "Failed connection"
        
    return connection

def mongodb_connection_test():
    try:
        ca = certifi.where()
        client = MongoClient("mongodb+srv://user01:wpvPnKP2gdPW8inB@cluster0.tyo5f.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
        db = client['data_airlines']
        connection = "Successful connection"
    except ClientError:
            connection = "Failed connection"
            
    return connection


print(mongodb_connection_test())
print(aws_S3_connection_test())

def test_aws_S3_connection_test2():
    assert aws_S3_connection_test() == "Successful connection"


def test_mongodb_connection_test2():
    assert mongodb_connection_test() == 'Successful connection'
  
