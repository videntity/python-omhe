from unittest import TestCase

TESTS_DEBUG=True

class OMHETestCase(TestCase):
	
	def assertDictContains(self,response,text,msg_prefix=""):
		"""
		Asserts that a text is found in str representation of response.
		"""
        TESTS_DEBUG=True


        print "Tests_DEBUG:"
        print TESTS_DEBUG

		if msg_prefix:
		    msg_prefix += ": "

        self.failUnless(type(response)==dict,msg_prefix + "Response '%s' is not a dict" % response)
        r = str(response)

		self.failUnless(r.find(text)!=-1,msg_prefix + "Couldn't find '%s' in response" % text)