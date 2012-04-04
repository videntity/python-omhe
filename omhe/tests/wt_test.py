from omhe.tests.OMHETestCase import OMHETestCase
import unittest
from omhe.core.parseomhe import parseomhe
from omhe.core.validators.validator_errors import *
from test_utils import *

"""

_wt_
*Weight*
weight
BETA
Use the 'k' suffix to denote kilograms.
Use the 'l' suffix to denote pounds(lbs).
Use '.' or 'p' to indicate 1/10ths of the weight unit.
# tags are allowed.
If the 'l' or 'k' is not supplied then the weight unit is inferred based on geography.
For example, pounds as a weight unit is implied in the United states.
wt125, wt=125l, wt85k, wt=155.5l, weight=134p7 wt170l#feel heavy

"""


TESTS_DEBUG = True


class wt_test(OMHETestCase):
    validValues = ('wt155', 'wt100', 'weight=60#tag','weight=75',
                   'weight=300k', 'weight=22l#tag','weight=800l')
    invalidOutOfRangeValues = ('weight=0','wt=#no weight just a tag', 'wt-10','wt-10k')
    invalidCommand = ('foo120/80p60#eee', 'bar=120','weigh=50','wieght=35')

    valid_parse_val_1="wt_numeric"


    if TESTS_DEBUG==True:
        print "================== START of WT TEST ================"


    def test_ValidValues_AlwaysContains_WeightNumericValue(self):
        """parse() of validValues should always return wt_numeric in dict."""

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