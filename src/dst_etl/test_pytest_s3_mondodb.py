import pytest
from function_test_s3_mongodb import *

def test_aws_S3_connection():
    assert aws_S3_connection() == "Successful connection"


def test_aws_mongodb_connection():
    assert aws_mongodb_connection() == 'Successful connection'
