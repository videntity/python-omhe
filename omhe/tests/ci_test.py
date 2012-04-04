__author__ = 'mark'


from omhe.core.parseomhe import parseomhe
from omhe.core.validators.validator_errors import *
from omhe.tests.OMHETestCase import OMHETestCase
from test_utils import *

import unittest
# OMHE Test Utilities

"""

_ci_
*Check In*
ci, checkin, check-in
BETA
# tags are allowed.	Check in to an OMHE service.
ci=Howdy Partner, checkin=Just ate a tofo.#lunch Gross!t


"""


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
                   'check-IN=weird checkin capitalization',
                   'checkin=#just a tag',
                   'CI=testing text handling for checkin to see if truncation is limted to matched terms in payload')
    validBlankValues = ('checkin=',
                               'checkin',
                               'ci=Y',
                               'checkin=10',
                               'checkin=11',
                               'CI=N',
                               'ci=y',)
    invalidCommand = ('foo35', 'bar=120',)


    valid_parse_val_1="ci"

    if TESTS_DEBUG==True:
        print "================== START of CI TEST ================"


    def test_ValidValues_AlwaysContains_CiContent(self):
        """parse() of validValues should always return ci value in dict."""
    
        if TESTS_DEBUG==True:
            display_function_info()
            display_data_set("Valid Values Set:",self.validValues)

    
        for i in self.validValues:
            p=parseomhe()
            result = p.parse(i)
    
            if TESTS_DEBUG==True:
                display_test_result(i,result)

            self.assertDictContains(result, self.valid_parse_val_1)


    def test_ValidBlankValues(self):
        """validate that blank values are also accepted. should return a dict."""
       
        if TESTS_DEBUG==True:
            display_function_info()
            display_data_set("Invalid Out of Range Values Set:",self.validBlankValues)

        for i in self.validBlankValues:
            p=parseomhe()
            d=p.split(i)
            print "output of split: [" + str(d) +"]"

            if TESTS_DEBUG==True:
                display_test_result(i,d)


            self.assertDictContains(d, self.valid_parse_val_1)


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