from omhe.tests.OMHETestCase import OMHETestCase
import unittest
from omhe.core.parseomhe import parseomhe

class bp_test(OMHETestCase):
    validValues = ('bp120/80', 'bp120/80p60', 'bp120/90p60#tag','bp=090090060',
                   'bloodpressure=140/90p70', 'bloodpressure100100090')
    valid_parse_val_1="bp_syst"
    valid_parse_val_2="bp_dia"

    def testValidValues(self):
        """toRoman should give known result with known input"""
        for i in self.validValues:
            p=parseomhe()
            result = p.parse(i)
            #print result
            k=result.keys()
            print k
            #if valid_parse_val_1 in k:
                #self.assertEqual("bp_sys", k)
            
            
            
            
if __name__ == "__main__":
    unittest.main()