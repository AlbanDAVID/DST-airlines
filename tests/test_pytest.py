import pytest
from function_test import *

def test_aws_connection():
    assert aws_connection() == "Successful connection"


def test_fetch_data_aws():
    assert fetch_data_aws() == 'successful data fetching'
