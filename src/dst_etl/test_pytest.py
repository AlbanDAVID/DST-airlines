import pytest
from function_test import *
from botocore.client import ClientError
import boto3
import certifi
from pymongo import MongoClient

def aws_S3_connection_test2():
    assert aws_S3_connection_test() == "Successful connection"


def mongodb_connection_test2():
    assert mongodb_connection_test() == 'Successful connection'
    
aws_S3_connection_test2()
mongodb_connection_test2()