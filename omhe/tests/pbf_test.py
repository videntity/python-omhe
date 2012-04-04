from omhe.tests.OMHETestCase import OMHETestCase
import unittest
from omhe.core.parseomhe import parseomhe
from omhe.core.validators.validator_errors import *
from test_utils import *

"""

_pbf_
*Percent Body Fat*
percentbodyfat
BETA
# tags are allowed
Used to record the percent of weight that is made up of body fat.
Valid range is 1-95.
pbf12.6 pbf=20, percentbodyfat=41#foo

"""

TESTS_DEBUG = True


class pbf_test(OMHETestCase):
    validValues = ('pbf12.6', 'pbf=15.60', 'percentbodyfat=30','percentbodyfat60','pbf=22.00001'
                   'pbf=25.54321', 'pbf=94.9999999', 'pbf=12#added comment' )
    invalidOutOfRangeValues = ('pbf=0.5','percentbodyfat=95.1', 'pbf=0.8#tags are accepted', 'pbf=15p5')
    invalidCommand = ('foo120/80p60#eee', 'bar=120')

    valid_parse_val_1="pbf_numeric"


    if TESTS_DEBUG==True:
        print "================== START of PBF TEST ================"


    def test_ValidValues_AlwaysContains_PBF_NumericValue(self):
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