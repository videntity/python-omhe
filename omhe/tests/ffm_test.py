__author__ = 'mark [AT] ekivemark [dot] com'

from omhe.tests.OMHETestCase import OMHETestCase
import unittest
from omhe.core.parseomhe import parseomhe
from omhe.core.validators.validator_errors import *
from test_utils import *

TESTS_DEBUG = True

"""
_ffm_
*Free Fat Mass*
freefatmass
BETA
'k' suffix indicates kilograms. 'l' suffix indicates lbs. lbs is assumed if no weight provided.
# tags are allowed	Used to express a body's free fat mass.
ffm12 ffm=20, ffm=20k, freefatmass=20l#foo

"""


class ffm_test(OMHETestCase):
    validValues = ('ffm30', 'ffm100', 'freefatmass=60#tag','freefatmass=60','freefatmass30',
                   'freefatmass=30', 'ffm=22', 'ffm30l', 'ffm=30k', 'ffm=30k#tag', 'ffm=30l#tag',
                   'freefatmass=0','freefatmass0')
    invalidOutOfRangeValues = ('ffm#message','ffm','ffm=#no value just hash')
    invalidCommand = ('foo120/80p60#eee', 'bar=120','freefat=100')

    valid_parse_val_1="ffm_numeric"

    if TESTS_DEBUG==True:
        print "================== START of FFM TEST ================"


    def test_ValidValues_AlwaysContains_FreeFatMass_NumericValue(self):
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