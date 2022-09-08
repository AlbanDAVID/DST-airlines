import pytest
from function_test import *

def aws_S3_connection():
    assert aws_S3_connection() == "Successful connection"


def aws_mongodb_connection():
    assert aws_mongodb_connection() == 'Successful connection'