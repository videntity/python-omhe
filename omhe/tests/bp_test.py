from omhe.tests.OMHETestCase import OMHETestCase
import unittest
from omhe.core.parseomhe import parseomhe
from omhe.core.validators.validator_errors import *

"""
_bp_
*Blood Pressure*
bloodpressure
BETA
Use either a 'd' or a front slash '/' to delineate between systolic and diastolic readings.
Either 'd' or '/' is required for a valid message.
Use 'p' to denote pulse. # tags are allowed.
The first number always represents systolic pressure.
The second number is always the diastolic pressure.
The third number is always pulse (if given).
# tags are allowed.
Range:
Systolic acceptable range: 50-400.
Diastolic acceptable range:20-200.
Pulse acceptable Range: 30-200.
bp90d123p70, bp=102d80p70, bp140d80p60, bp=140/80p60, bp=120080060

"""


TESTS_DEBUG = True

class bp_test(OMHETestCase):
    validValues = ('bp120/80', 'bp120/80p60', 'bp120/90p60#tag','bp=090090060',
                   'bloodpressure=140/90p70', 'bloodpressure100100090')
    invalidOutOfRangeValues = ('bp1200/80p60','bp#no values just a tag')
    invalidCommand = ('foo120/80p60', 'bar=120000p60',) 

    valid_parse_val_1="bp_sys"
    valid_parse_val_2="bp_dia"

    if TESTS_DEBUG==True:
        print "================== START of BP TEST ================"

    def testValidValuesAlwayscontainsSystolicValue(self):
        """parse() of validValues should always return bp_sys in dict."""
        for i in self.validValues:
            p=parseomhe()
            result = p.parse(i)
            if TESTS_DEBUG==True:
                print " "
                print "Testing Value:" + str(i)
                print "parsed result:"
                print result
                print "end of Parsed Result"

            self.assertDictContains(result, self.valid_parse_val_1)
            
    def testValidValuesAlwayscontainsDiastolicValue(self):
        """parse() of validValues should always return bp_dia in dict."""
        for i in self.validValues:
            p=parseomhe()
            result = p.parse(i)
            if TESTS_DEBUG==True:
                print " "
                print "Testing Value:" + str(i)
                print "parsed result:"
                print result
                print "end of Parsed Result"

            self.assertDictContains(result, self.valid_parse_val_2)
            
    def testInvalidOutOfRangeValues(self):
        """validate() of invalidOutOfRangeValues should always raise InvalidValueError."""
        for i in self.invalidOutOfRangeValues:
            p=parseomhe()
            d=p.split(i)
            if TESTS_DEBUG==True:
                print " "
                print "Testing Out of Range Value:" + str(i)
                print "parsed result(d):"
                print d
                print "end of Parsed Result"

            self.assertRaises(InvalidValueError, p.validate, splitdict=d)
    
    def testInvalidMessageRaisesInvalidMessageError(self):
        """split() of invalidCommand should always raise InvalidMessageError."""
        for i in self.invalidCommand:
            p=parseomhe()
            if TESTS_DEBUG==True:
                print "Testing Invalid Command:" + str(i)
                print p
                print "End of parsed result"
            
            self.assertRaises(InvalidMessageError, p.split, message=i)
            
            
if __name__ == "__main__":
    unittest.main()