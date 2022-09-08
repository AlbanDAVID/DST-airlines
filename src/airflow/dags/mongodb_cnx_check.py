from botocore.client import ClientError
import boto3
import certifi
from pymongo import MongoClient


def mongodb_connection_test():
    try:
        ca = certifi.where()
        client = MongoClient("mongodb+srv://user01:wpvPnKP2gdPW8inB@cluster0.tyo5f.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
        db = client['data_airlines']
        connection = "Successful connection"
    except ClientError:
            connection = "Failed connection"
            
    print(connection)

