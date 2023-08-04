#Jue Wu
#12/6/2022
#CS5001
#Final Project
#Test BinaryKnitting Class

from BinaryKnitting import BinaryKnitting
import unittest

class BinaryKnittingTest(unittest.TestCase):
    def test_init(self):
        knit = BinaryKnitting("a")
        self.assertEqual(knit.message, "a")
    
    def test_knit(self):
        knit = BinaryKnitting('a')
        result = knit.knit()
        self.assertIsInstance(result, list)

    def test_pattern(self):
        knit = BinaryKnitting('a')
        result = knit.pattern('a')
        self.assertIsInstance(result, str)

def main():
    unittest.main()
    

main()