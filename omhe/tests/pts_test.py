__author__ = 'mark'

from omhe.tests.OMHETestCase import OMHETestCase
import unittest
from omhe.core.parseomhe import parseomhe
from omhe.core.validators.validator_errors import *
from test_utils import *

"""

_pts_
*Points*
points, gems
# tags are allowed
Points or rewards
Range: negative or positive integer
pts=-50, points=100 points

"""


TESTS_DEBUG = True


class pts_test(OMHETestCase):
    validValues = ('pts10', 'pts=1005', 'pts=-50', 'pts=2000','gems=500',
                   'points=200', 'points250','gems-100','points=-90', 'pts=0')
    invalidOutOfRangeValues = ('pts=400.35','points=150.6#tags','pts=200#no tags')
    invalidCommand = ('foo120/80p60#eee', 'bar=120','gem=50','point=35')

    valid_parse_val_1="points"


    if TESTS_DEBUG==True:
        print "================== START of PTS TEST ================"


    def test_ValidValues_AlwaysContains_Points_NumericValue(self):
        """parse() of validValues should always return points in dict."""

        if TESTS_DEBUG==True:
            display_function_info()
            display_data_set("Valid Values Set:",self.validValues)

        for i in self.validValues:
            p=parseomhe()
            result = p.parse(i)
            if TESTS_DEBUG==True:
                display_test_result(i,result)

            self.assertDictContains(result, self.valid_parse_val_1)
            
            
    def test_Invalid_OutOfRangeValues(self):
        """validate() of invalidOutOfRangeValues should always raise InvalidValueError."""

        if TESTS_DEBUG==True:
            display_function_info()
            display_data_set("Invalid Out of Range Values Set:",self.invalidOutOfRangeValues)


        for i in self.invalidOutOfRangeValues:
            p=parseomhe()
            d=p.split(i)

            if TESTS_DEBUG==True:
                display_test_result(i,d)


            self.assertRaises(InvalidValueError, p.validate, splitdict=d)
    
    def test_InvalidMessage_Raises_InvalidMessageError(self):
        """split() of invalidCommand should always raise InvalidMessageError."""

        if TESTS_DEBUG==True:
            display_function_info()
            display_data_set("Invalid Command Set:",self.invalidCommand)

        for i in self.invalidCommand:
            p=parseomhe()

            if TESTS_DEBUG==True:
                display_test_result(i,p)

            self.assertRaises(InvalidMessageError, p.split, message=i)
            
            
if __name__ == "__main__":
    unittest.main()