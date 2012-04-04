__author__ = 'mark'


from omhe.core.parseomhe import parseomhe
from omhe.core.validators.validator_errors import *
from omhe.tests.OMHETestCase import OMHETestCase
from test_utils import *

import unittest
# OMHE Test Utilities

"""

_frv_
*freggies*
frv, freggie
BETA
No # tags allowed.
Record a fruit or vegetable eaten. One fruit or vegetable per message.
frv=strawberry, freggie=Passionfruit


"""

TESTS_DEBUG = True


class frv_test(OMHETestCase):
    """
    _frv_
    *freggies*
    frv, freggie
    BETA
    No # tags allowed.
    Record a fruit or vegetable eaten. One fruit or vegetable per message.
    frv=strawberry, freggie=passionfruit
    """

    TESTS_DEBUG = True

    validValues = ('frv=apple', 'freggie=apricot', 'frv=avocado', 'freggie=banana', 'frv=blackberry', 'frvblueberry',
                   'freggiecherry', 'frvcoconut', 'frv=crabapple', 'frv=cranberry', 'frv=grapefruit',
                   'frv=grapes', 'frv=keyLime', 'frv=kiwi', 'frv=lemon', 'frv=lime', 'frv=mandarin',
                   'frv=mango', 'frv=melon', 'frv=mulberry', 'frv=nectarines', 'frv=olive', 'frv=orange',
                   'frv=papaya', 'frv=passionfruit', 'frv=peach', 'frv=pear', 'frv=pineapple', 'frv=plum',
                   'frv=pomegranate', 'frv=raspberry', 'frv=strawberry', 'frv=tangerine', 'frv=tomato',
                   'frv=watermelon', 'frv=asparagus', 'frv=beets', 'frv=bell pepper', 'frv=broccoli',
                   'frv=brussels sprouts', 'frv=cabbage', 'frv=carrots', 'frv=cauliflower', 'frv=celery',
                   'frv=collard greens', 'frv=corn', 'frv=cucumbers', 'frv=eggplant', 'frv=garlic',
                   'frv=green beans', 'frv=green peas', 'frv=kale', 'frv=mushrooms', 'frv=okra',
                   'frv=olives', 'frv=onions', 'frv=parsnips', 'frv=potatoes', 'frv=pumpkin',
                   'frv=romaine lettuce', 'frv=spinach', 'frv=squash', 'frv=sweet potatoes',
                   'frv=turnip greens', 'frv=watercress', 'frv=yams', 'frv=zucchini', 'frv=other',
                    'frv=Turnip', 'freggie=Passionfruit', 'frv=cucumber', 'frv=CUCUMBER','frv=Nectarine'
                    )

    invalidOutOfRangeValues = ('frv=CUCUMBER', 'freggie=CrabApple',
                               'frv=Crab Apples', 'freggie=crabApples')
    validBlankValues = ('frv=',
                        'freggie',
                        'FRV=',
                        'FREGGIE=',
                        'frv',
                        )
    invalidCommand = ('foo35', 'bar=120',)


    valid_parse_val_1="frv"

    if TESTS_DEBUG==True:
        print "================== START of FRV TEST ================"


    def test_ValidValues_AlwaysContains_FrvContent(self):
        """parse() of validValues should always return frv value in dict."""
    
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