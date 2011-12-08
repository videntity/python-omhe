import re,sys
from validator_errors import *




freggies=('apple', 'apricot', 'avocado', 'banana', 'blackberry', 'blueberry',
          'cherry', 'coconut', 'crabapple', 'cranberry', 'grapefruit',
          'grapes', 'keyLime', 'kiwi', 'lemon', 'lime', 'mandarin',
          'mango', 'melon', 'mulberry', 'nectarines', 'olive', 'orange',
          'papaya', 'passionfruit', 'peach', 'pear', 'pineapple', 'plum',
          'pomegranate', 'paspberry', 'strawberry', 'tangerine', 'tomato',
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
        error_msg="%s is not a valid fruit of veggie." % (freggiename)
        raise InvalidMessageError(error_msg)

    return valdict
