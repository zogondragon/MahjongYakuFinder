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
        self.assertEqual(self.hnc.ConvertTextToSetNotation("11122233344455m"), 
            "3333200000000000000000000000000000")
        self.assertEqual(self.hnc.ConvertTextToSetNotation("11122233344455s"), 
            "0000000003333200000000000000000000")
        self.assertEqual(self.hnc.ConvertTextToSetNotation("11122233344455p"), 
            "0000000000000000003333200000000000")
        self.assertEqual(self.hnc.ConvertTextToSetNotation("2478m111s899pESSR"), 
            "0101001103000000000000000121200001")
        self.assertEqual(self.hnc.ConvertTextToSetNotation("19m19s19pESWNBGGR"), 
            "1000000011000000011000000011111121")
        self.assertEqual(self.hnc.ConvertTextToSetNotation("114477m2266sEENN"), 
            "2002002000200020000000000002002000")
        self.assertEqual(self.hnc.ConvertTextToSetNotation(""), None)
        self.assertEqual(self.hnc.ConvertTextToSetNotation("slIGho328jhs@$!"), None)
        self.assertEqual(self.hnc.ConvertTextToSetNotation("111112222233333m"), None)
        self.assertEqual(self.hnc.ConvertTextToSetNotation("1111222233334m"), None)
        self.assertEqual(self.hnc.ConvertTextToSetNotation("111122223333333m"), None)
        self.assertEqual(self.hnc.ConvertTextToSetNotation("5544433322211m"), None)
        self.assertEqual(self.hnc.ConvertTextToSetNotation("2478m111s899pEGNR"), None)
        self.assertEqual(self.hnc.ConvertTextToSetNotation("2478m11155s899pESSR"), None)
        self.assertEqual(self.hnc.ConvertTextToSetNotation("2478p111s899mESSR"), None)
        self.assertEqual(self.hnc.ConvertTextToSetNotation("ESSR2478m111s899p"), None)
        self.assertEqual(self.hnc.ConvertTextToSetNotation("2478m11155m899mESSR"), None)
        self.assertEqual(self.hnc.ConvertTextToSetNotation("2478s11155s899sESSR"), None)
        self.assertEqual(self.hnc.ConvertTextToSetNotation("2478s11155p899pESSR"), None)

    def test_ConvertSetToTextNotation(self):
        self.assertEqual(self.hnc.ConvertSetToTextNotation("1110000001110000001110000003200000"), 
            "123m123s123pEEESS")
        self.assertEqual(self.hnc.ConvertSetToTextNotation("3333200000000000000000000000000000"), 
            "11122233344455m")
        self.assertEqual(self.hnc.ConvertSetToTextNotation("0000000003333200000000000000000000"), 
            "11122233344455s")
        self.assertEqual(self.hnc.ConvertSetToTextNotation("0000000000000000003333200000000000"), 
            "11122233344455p")
        self.assertEqual(self.hnc.ConvertSetToTextNotation("0101001103000000000000000121200001"), 
            "2478m111s899pESSR")
        self.assertEqual(self.hnc.ConvertSetToTextNotation("1000000011000000011000000011111121"), 
            "19m19s19pESWNBGGR")
        self.assertEqual(self.hnc.ConvertSetToTextNotation("2002002000200020000000000002002000"), 
            "114477m2266sEENN")
        self.assertEqual(self.hnc.ConvertSetToTextNotation("3002002000200020000000000002002000"), 
            None)       # 15-tile hand
        self.assertEqual(self.hnc.ConvertSetToTextNotation("1002002000200020000000000002002000"), 
            None)       # 13-tile hand
        self.assertEqual(self.hnc.ConvertSetToTextNotation("20020020002000200000000000020020002"), 
            None)       # Invalid set notation
        self.assertEqual(self.hnc.ConvertSetToTextNotation("200200200020002000000000000200200"), 
            None)       # Invalid set notation

    def test_VerifyTextNotation(self):
        self.assertEqual(self.hnc.VerifyTextNotation(""), False)                     # Empty string
        self.assertEqual(self.hnc.VerifyTextNotation("slIGho37728jhs@$!"), False)    # Gibberish string
        self.assertEqual(self.hnc.VerifyTextNotation("slIGho328jhs@$!"), False)      # Gibberish string
        self.assertEqual(self.hnc.VerifyTextNotation("123m123s123pEEESS"), True)     # Good hand
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
