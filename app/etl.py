from queries import *
from utils import *

# QUERIES API AIRLBAS
test = getFlightAirlabs('LH2001')
test_response = test.print_request()
print(test_response)
