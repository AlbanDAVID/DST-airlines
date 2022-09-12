import pytest

from botocore.client import ClientError
import boto3
import certifi
from pymongo import MongoClient
import static


def aws_S3_connection_test():
    
    try:
        s3_client = boto3.client('s3', aws_access_key_id= static.aws_access_key_id,aws_secret_access_key=static.aws_secret_access_key)
        response = s3_client.list_objects_v2(Bucket='datalake-airlines', Prefix='01-real-time-flights-airlabs/')
        connection = "Successful connection"
    except :
        connection = "Failed connection"
        
    return connection

def mongodb_connection_test():
    try:
        ca = certifi.where()
        client = MongoClient(static.cnx_mongodb, tlsCAFile=ca)
        db = client['data_airlines']
        connection = "Successful connection"
    except ClientError:
            connection = "Failed connection"
            
    return connection


print(mongodb_connection_test())
print(aws_S3_connection_test())

def test_aws_S3_connection_test():
    assert aws_S3_connection_test() == "Successful connection"


def test_mongodb_connection_test():
    assert mongodb_connection_test() == 'Successful connection'
  
