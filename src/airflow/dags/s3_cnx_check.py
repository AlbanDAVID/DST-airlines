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
        
    print(connection)

