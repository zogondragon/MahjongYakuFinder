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

    def test_VerifyTextNotation(self):
        self.assertEqual(self.hnc.VerifyTextNotation("slIGho328jhs@$!"), False)      # Gibberish string
        self.assertEqual(self.hnc.VerifyTextNotation("11122233344455m"), True)       # Good hand
        self.assertEqual(self.hnc.VerifyTextNotation("111112222233333m"), False)     # 15-tile hand
        self.assertEqual(self.hnc.VerifyTextNotation("1111222233334m"), False)       # 13-tile hand
        self.assertEqual(self.hnc.VerifyTextNotation("111122223333333m"), False)     # More than 4 tiles of 3m
        self.assertEqual(self.hnc.VerifyTextNotation("5544433322211m"), False)       # Not sorted 
        self.assertEqual(self.hnc.VerifyTextNotation("11122233344455s"), True)       # Good hand
        self.assertEqual(self.hnc.VerifyTextNotation("11122233344455p"), True)       # Good hand
        self.assertEqual(self.hnc.VerifyTextNotation("2478m111s899pESSR"), True)     # Good hand
        self.assertEqual(self.hnc.VerifyTextNotation("2478m111s899pEGNR"), False)    # Not sorted
        self.assertEqual(self.hnc.VerifyTextNotation("2478m11155s899pESSR"), False)  # 16-tile hand
        self.assertEqual(self.hnc.VerifyTextNotation("2478p111s899mESSR"), False)    # Not sorted
        self.assertEqual(self.hnc.VerifyTextNotation("ESSR2478m111s899p"), False)    # Not sorted
        self.assertEqual(self.hnc.VerifyTextNotation("2478m11155m899mESSR"), False)  # Multiple Man tiles
        self.assertEqual(self.hnc.VerifyTextNotation("2478s11155s899sESSR"), False)  # Multiple Sak tiles
        self.assertEqual(self.hnc.VerifyTextNotation("2478s11155p899pESSR"), False)  # Multiple Ping tiles
            
if __name__ == '__main__':
    unittest.main()
