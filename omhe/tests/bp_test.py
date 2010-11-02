from omhe.tests.OMHETestCase import OMHETestCase
import unittest
from omhe.core.parseomhe import parseomhe
from omhe.validators.validator_errors import *

class bp_test(OMHETestCase):
    validValues = ('bp120/80', 'bp120/80p60', 'bp120/90p60#tag','bp=090090060',
                   'bloodpressure=140/90p70', 'bloodpressure100100090')
    invalidOutOfRangeValues = ('bp1200/80p60',)    

    valid_parse_val_1="bp_syst"
    valid_parse_val_2="bp_dia"

    def testValidValues(self):
        """parseomhe of validValues should always return bp_sys in dict."""
        for i in self.validValues:
            p=parseomhe()
            result = p.parse(i)
            self.assertDictContains(result, "bp_sys")
            
    def testInvalidOutOfRangeValues(self):
        """parseomhe of invalideOutOfRangevlues should always raise ."""
        for i in self.invalidOutOfRangeValues:
            p=parseomhe()
            #result = p.parse(i)
            #print result
            #k=result.keys()
            #print k
            self.assertRaises(InvalidValueError, p.parse, message=i)
            
            
if __name__ == "__main__":
    unittest.main()