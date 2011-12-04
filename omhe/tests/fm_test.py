from omhe.tests.OMHETestCase import OMHETestCase
import unittest
from omhe.core.parseomhe import parseomhe
from omhe.core.validators.validator_errors import *

class fm_test(OMHETestCase):
    validValues = ('fm30', 'fm100', 'fatmass=60#tag','fatmass=60',
                   'fatmass=30', 'fm=22')
    invalidOutOfRangeValues = ('fm0',)
    invalidCommand = ('foo120/80p60#eee', 'bar=120',) 

    valid_parse_val_1="fm_numeric"

    def testValidValuesAlwayscontainsFatMassNumericValue(self):
        """parse() of validValues should always return fm_mumeric in dict."""
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