__author__ = 'mark [AT] ekivemark [dot] com'


from omhe.tests.OMHETestCase import OMHETestCase
import unittest
from omhe.core.parseomhe import parseomhe
from omhe.core.validators.validator_errors import *
from test_utils import *

TESTS_DEBUG = True

"""
Command=bg
Name=Blood Glucose Level
Alias=bloodglucose
Status=BETA
Options=Only # tags are allowed.
Notes=Used to express a blood glucose level.
Range=0-500
Examples=bg120, bg135, bg=124, bg200#off the charts today

"""


class bg_test(OMHETestCase):
    validValues = ('bg120', 'bg100#note', 'bg=399#Almost at limit','bg=80',
                   'bloodglucose=140', 'bloodglucose200')
    invalidOutOfRangeValues = ('bg501', 'bg=#nothing just a tag','bg=', 'bg=-01','bg=501','bloodglucose=-1','bloodglucose-1','bg-1','bg=-10')
    invalidCommand = ('foo120/80p60', 'bar=120000p60','blood=20')

    valid_parse_val_1="bg"


    if TESTS_DEBUG==True:
        print "================== START of BG TEST ================"

    def test_ValidValues_AlwaysContains_bg_Value(self):
        """parse() of validValues should always return bg in dict."""

        if TESTS_DEBUG==True:
            display_function_info()
            display_data_set("Valid Values Set:",self.validValues)

        for i in self.validValues:
            p=parseomhe()
            result = p.parse(i)
            if TESTS_DEBUG==True:
                display_test_result(i,result)

            self.assertDictContains(result, self.valid_parse_val_1)
            
    def test_InvalidOutOfRangeValues(self):
        """validate() of invalidOutOfRangeValues should always raise InvalidValueError."""

        if TESTS_DEBUG==True:
            display_function_info()
            display_data_set("Invalid Out of Range Values Set:",self.invalidOutOfRangeValues)


        for i in self.invalidOutOfRangeValues:
            p=parseomhe()
            if TESTS_DEBUG==True:
                print "parseomhe result:"
                print p
                print p.validate

            d=p.split(i)
            if TESTS_DEBUG==True:
                print "output of split: [" + str(d) +"]"

            if TESTS_DEBUG==True:
                display_test_result(i,d)

            self.assertRaises(InvalidValueError, p.validate, splitdict=d)
    
    def testInvalidMessageRaisesInvalidMessageError(self):
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