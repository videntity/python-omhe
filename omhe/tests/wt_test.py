from omhe.tests.OMHETestCase import OMHETestCase
import unittest
from omhe.core.parseomhe import parseomhe
from omhe.core.validators.validator_errors import *

class wt_test(OMHETestCase):
    validValues = ('wt155', 'wt100', 'weight=60#tag','weight=75',
                   'weight=300k', 'weight=22l#tag')
    invalidOutOfRangeValues = ('weight=2',)
    invalidCommand = ('foo120/80p60#eee', 'bar=120',) 

    valid_parse_val_1="wt_numeric"

    def testValidValuesAlwayscontainsWeightNumericValue(self):
        """parse() of validValues should always return wt_mumeric in dict."""
        for i in self.validValues:
            p=parseomhe()
            result = p.parse(i)
            self.assertDictContains(result, self.valid_parse_val_1)
            
            
    def testInvalidOutOfRangeValues(self):
        """validate() of invalideOutOfRangevlues should always raise InvalidValueError."""
        for i in self.invalidOutOfRangeValues:
            p=parseomhe()
            d=p.split(i)
            self.assertRaises(InvalidValueError, p.validate, splitdict=d)
    
    def testInvalidMessageRaisesInvalidMessageError(self):
        """split() of invalidCommand should always raise InvalidMessageError."""
        for i in self.invalidCommand:
            p=parseomhe()
            self.assertRaises(InvalidMessageError, p.split, message=i)
            
            
if __name__ == "__main__":
    unittest.main()