from unittest import TestCase


class OMHETestCase(TestCase):
	
	def assertContains(self, response, text, count=None, status_code=200,
                       msg_prefix=''):
		"""
		Asserts that a response indicates that a page was retrieved
		successfully, (i.e., the HTTP status code was as expected), and that
		``text`` occurs ``count`` times in the content of the response.
		If ``count`` is None, the count doesn't matter - the assertion is true
		if the text occurs at least once in the response.
		"""
		if msg_prefix:
		    msg_prefix += ": "
	
		self.assertEqual(response.status_code, status_code,
		    msg_prefix + "Couldn't retrieve page: Response code was %d"
		    " (expected %d)" % (response.status_code, status_code))
		text = smart_str(text, response._charset)
		real_count = response.content.count(text)
		if count is not None:
		    self.assertEqual(real_count, count,
			msg_prefix + "Found %d instances of '%s' in response"
			" (expected %d)" % (real_count, text, count))
		else:
		    self.failUnless(real_count != 0,
			msg_prefix + "Couldn't find '%s' in response" % text)
