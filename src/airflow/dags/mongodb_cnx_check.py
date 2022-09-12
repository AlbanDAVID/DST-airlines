from botocore.client import ClientError
import boto3
import certifi
from pymongo import MongoClient
import static


def mongodb_connection_test():
    try:
        ca = certifi.where()
        client = MongoClient(static.cnx_mongodb, tlsCAFile=ca)
        db = client['data_airlines']
        connection = "Successful connection"
    except ClientError:
            connection = "Failed connection"
            
    print(connection)

