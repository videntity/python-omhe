__author__ = 'mark'


from omhe.core.parseomhe import parseomhe
from omhe.core.validators.validator_errors import *
from omhe.tests.OMHETestCase import OMHETestCase
import unittest

TESTS_DEBUG = True


class ci_test(OMHETestCase):
    """
    Command: ci
    Name: Check In
    Known Alias: ci, checkin, check-in, check
    Status: BETA
    Options: # tags are allowed.
    Notes: Start using a service
    Examples: ci=Howdy Partner, checkin=Just ate a tofo.#lunch Gross!
    """

    TESTS_DEBUG = True

    validValues = ('ci=Howdy OMHE',
                   'check-in=A simple check-in',
                   'checkin=A simple checkin',
                   'check=You can use Check to Checkin',
                   'CI=Checkin in capitals',
                   'CHECKIN=All Capitals for Checkin',
                   'Check-In=First Capital Check-In',
                   'check-IN=weird checkin capitalization')
    invalidOutOfRangeValues = ('checkin=',
                               'checkin',
                               'ci=Y',
                               'CI=N')
    invalidCommand = ('foo35', 'bar=120',)


    valid_parse_val_1="ci"

    def testValidValuesAlwaysContainsFatMassNumericValue(self):
        """parse() of validValues should always return ci value in dict."""
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