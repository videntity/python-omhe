from omhe.tests.OMHETestCase import OMHETestCase
import unittest
from omhe.core.parseomhe import parseomhe
from omhe.core.validators.validator_errors import *
from test_utils import *

"""

_md_
*Mood*
mood
BETA
No # tags allowed.
Level of happiness, mood,
or general feeling of well being on a scale of 0-10.
Range:0=none, 10=max
mood9, mood=1, md1, md=10

"""

TESTS_DEBUG = True


class md_test(OMHETestCase):
    validValues = ('md0', 'md=1', 'mood=2','mood3','md=4'
                   'md=5', 'md6','mood7','mood=8','md=9', 'mood=10' )
    invalidOutOfRangeValues = ('md-1','mood11' 'md=5#tags not accepted', 'md=5.5','mood=6p4')
    invalidCommand = ('foo120/80p60#eee', 'bar=120','mod=5', 'moods=9')

    valid_parse_val_1="md_numeric"


    if TESTS_DEBUG==True:
        print "================== START of MD TEST ================"


    def test_ValidValues_AlwaysContains_Mood_NumericValue(self):
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