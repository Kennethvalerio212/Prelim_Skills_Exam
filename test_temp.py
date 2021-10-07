import unittest
from Temp import Temperature

class myTest(unittest.TestCase):

    def test_invalid(self):
        # test where values < 0
        
        self.assertRaises(ValueError,Temperature,-2)   

def test_valid(self):
        # test where values > 0
        
        self.assertGreater(0,Temperature,1 

if __name__ == '__main__' :
    unittest.main()