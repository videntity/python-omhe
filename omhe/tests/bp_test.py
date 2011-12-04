from omhe.tests.OMHETestCase import OMHETestCase
import unittest
from omhe.core.parseomhe import parseomhe
from omhe.core.validators.validator_errors import *

class bp_test(OMHETestCase):
    validValues = ('bp120/80', 'bp120/80p60', 'bp120/90p60#tag','bp=090090060',
                   'bloodpressure=140/90p70', 'bloodpressure100100090')
    invalidOutOfRangeValues = ('bp1200/80p60',)
    invalidCommand = ('foo120/80p60', 'bar=120000p60',) 

    valid_parse_val_1="bp_syst"
    valid_parse_val_2="bp_dia"

    def testValidValuesAlwayscontainsSystolicValue(self):
        """parse() of validValues should always return bp_syst in dict."""
        for i in self.validValues:
            p=parseomhe()
            result = p.parse(i)
            self.assertDictContains(result, self.valid_parse_val_1)
            
    def testValidValuesAlwayscontainsDiastolicValue(self):
        """parse() of validValues should always return bp_dia in dict."""
        for i in self.validValues:
            p=parseomhe()
            result = p.parse(i)
            self.assertDictContains(result, self.valid_parse_val_2)
            
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