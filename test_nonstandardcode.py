import unittest
from your_package import nonstandardcode

class TestNonstandardCode(unittest.TestCase):
    def test_functionality(self):
	# Add your tests here 
	self.assertTrue(True)


if __name__=='__main__':
    unittest.main()
