__author__ = 'mark [AT] ekivemark [dot] com'

from omhe.tests.OMHETestCase import OMHETestCase
import unittest
from omhe.core.parseomhe import parseomhe
from omhe.core.validators.validator_errors import *
from test_utils import *

TESTS_DEBUG = True

"""
_fm_
*Fat Mass*
fatmass
BETA
'k' suffix indicates kilograms. 'l' suffix indicates lbs. lbs is assumed if no weight provided.
# tags are allowed	Used to express a body fat mass.
fm12 fm=20, fm=20k, fatmass=20l#foo

"""


class fm_test(OMHETestCase):
    validValues = ('fm30', 'fm100', 'fatmass=60#tag','fatmass=60',
                   'fatmass=30', 'fm=22', 'fm30l', 'fm=30k', 'fm=30k#tag', 'fm=30l#tag')
    invalidOutOfRangeValues = ('fm0',)
    invalidCommand = ('foo120/80p60#eee', 'bar=120',) 

    valid_parse_val_1="fm_numeric"

    if TESTS_DEBUG==True:
        print "================== START of FM TEST ================"


    def test_ValidValues_AlwaysContains_FatMass_NumericValue(self):
        """parse() of validValues should always return fm_numeric in dict."""
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