__author__ = 'mark'

import inspect

"""
Add frequently used test routines to this file.

Add import statement to {cmd}_test.py to include.

"""

class term_color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''


def display_function_info():

    caller = inspect.getframeinfo(inspect.currentframe().f_back)[2]

    print ""
    print term_color.OKGREEN+"{0}:{1}".format(inspect.getframeinfo(inspect.currentframe().f_back)[0], caller) +term_color.ENDC

    return

def display_data_set(message="Command Set",display_set=('Nothing to evaluate')):

    print message
    print "========= START OF SET ========="
    print display_set
    print "========== END OF SET =========="
    print " "

    return

def display_test_result(value_tested="Empty",outcome="No Result"):

    print "Testing Value: [" + str(value_tested) +"]"
    print "======= start of result ======="
    print outcome
    print "======== end of Result ========"
    print " "

    return