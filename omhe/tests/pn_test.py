__author__ = 'mark'

from omhe.tests.OMHETestCase import OMHETestCase
import unittest
from omhe.core.parseomhe import parseomhe
from omhe.core.validators.validator_errors import *
from test_utils import *

"""

_pn_
*Pain*
pain
BETA
# tags are allowed.
Pain (general) on a scale of 0-10.
Range:0=none, 10=max
pain=0, pain9#back, pain=5#neck

"""

TESTS_DEBUG = True


class pn_test(OMHETestCase):
    validValues = ('pn0', 'pn=1', 'pain=2','pain3','pn=4#back'
                   'pn=5', 'pn6#again','pain7','pain=8#Neck','pn=9', 'pain=10#excrusiating' )
    invalidOutOfRangeValues = ('pn-1','pain11' , 'pn=5.5','pain=6p4')
    invalidCommand = ('foo120/80p60#eee', 'bar=120','mod=5', 'painful=9')

    valid_parse_val_1="pn_numeric"


    if TESTS_DEBUG==True:
        print "================== START of PN TEST ================"


    def test_ValidValues_AlwaysContains_Pain_NumericValue(self):
        """parse() of validValues should always return md_numeric in dict."""

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