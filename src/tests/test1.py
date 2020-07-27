
import unittest
from PyScripts import HelloWorld

class TestValidator(unittest.TestCase):

	def test_reject_string_if_lomg(self):
		smpl_str = "Hello"
		result = HelloWorld.sample(smpl_str)
		self.assertTrue(result)


if __name__ == '__main__':
	unittest.main()