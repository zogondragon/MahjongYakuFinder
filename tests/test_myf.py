import unittest
from src.MahjongYakuFinder import myf

class TestHandNotationConverter(unittest.TestCase):
    def setUp(self):
        self.hnc = myf.HandNotationConverter()

    def tearDown(self):
        self.hnc = None

    def test_ConvertTextToSetNotation(self):
        self.assertEqual(self.hnc.ConvertTextToSetNotation("123m123s123pEEESS"), 
            "1110000001110000001110000003200000")
            
if __name__ == '__main__':
    unittest.main()