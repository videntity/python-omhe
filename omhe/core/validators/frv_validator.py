import re,sys
from validator_errors import *

"""
fixes for Freggies function

Source Dict (freggies) list of Fruit and vegetables should be in singular form
freggies list should be stored in lower case with no spaces between multiple word descriptors.
e.g. store "passion fruit" and "crab apples" as "passionfruit" and "crabapple".

Test should lower(singularize(freggiename)) input before testing if contained in dict
ie. singularize and convert to lower case then compare to see if contained in list.

Recommend delimiting multiple input with commas and
then removing spaces from each value to be evaluated before testing.

"""



freggies=('apple', 'apricot', 'avocado', 'banana', 'blackberry', 'blueberry',
          'cherry', 'coconut', 'crabapple', 'cranberry', 'grapefruit',
          'grapes', 'keylime', 'kiwi', 'lemon', 'lime', 'mandarin',
          'mango', 'melon', 'mulberry', 'nectarines', 'olive', 'orange',
          'papaya', 'passionfruit', 'peach', 'pear', 'pineapple', 'plum',
          'pomegranate', 'raspberry', 'strawberry', 'tangerine', 'tomato',
          'watermelon', 'asparagus', 'beets', 'bell pepper', 'broccoli',
          'brussels sprouts', 'cabbage', 'carrots', 'cauliflower', 'celery',
          'collard greens', 'corn', 'cucumbers', 'eggplant', 'garlic',
          'green beans', 'green peas', 'kale', 'mushrooms', 'okra',
          'olives', 'onions', 'parsnips', 'potatoes', 'pumpkin',
          'romaine lettuce', 'spinach', 'squash', 'sweet potatoes',
          'turnip greens', 'watercress', 'yams', 'zucchini', 'other')




def frv_validator(omhe_value):
    valdict={}
    if omhe_value[0] == "=":
        omhe_value=omhe_value[1:]
        
    if omhe_value[-1].isdigit():
        valdict[omhe_value[:-1]]=str(omhe_value[-1])
        freggiename=omhe_value[:-1]
    else:
        valdict[omhe_value[:]]="1"
        freggiename=omhe_value[:]
    
    if freggies.__contains__(freggiename)==False:
        error_msg="%s is not a valid fruit or veggie." % (freggiename)
        raise InvalidMessageError(error_msg)

    return valdict
