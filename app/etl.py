from queries import *
from utils import *

# QUERIES API AIRLBAS
"""
test = getFlightAirlabs('LH2001')
test_response = test.print_request()
print(test_response)
"""

# QUERIES API LUFTHANSA
"""
test = getFlightInfoLuf('LH1290', '2022-07-21')
test.get_result()
"""

test = getFlightInfoByRouteLuf('FRA', 'JTR', '2022-07-21')
test.get_result()
