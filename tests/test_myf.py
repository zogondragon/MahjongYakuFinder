import unittest
from src.MahjongYakuFinder import myf

class TestHandAndYaku(unittest.TestCase):
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
        self.assertEqual(self.hnc.ConvertSetToTextNotation(""), 
            None)       # Empty set notation
        self.assertEqual(self.hnc.ConvertSetToTextNotation("aowegihwaoegihweglwjgweoigh!(*^@123"), 
            None)       # Gibberish set notation
        self.assertEqual(self.hnc.ConvertSetToTextNotation("aowegihwaogihweglwjgweoigh!(*^@123"), 
            None)       # Gibberish set notation

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

    def test_YakuKokushimusou(self):
        yaku = myf.YakuKokushimusou()
        hands = []
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("119m19s19pESWNBGR")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("199m19s19pESWNBGR")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("19m119s19pESWNBGR")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("19m199s19pESWNBGR")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("19m19s119pESWNBGR")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("19m19s199pESWNBGR")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("19m19s19pEESWNBGR")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("19m19s19pESSWNBGR")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("19m19s19pESWWNBGR")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("19m19s19pESWNNBGR")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("19m19s19pESWNBBGR")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("19m19s19pESWNBGGR")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("19m19s19pESWNBGRR")))
        for hand in hands:
            self.assertEqual(yaku.CheckHand(hand), True)
        invalid_hands = []
        invalid_hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("111m19s19pESWNBGR")))
        invalid_hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("789m19s19pESWNBGR")))
        invalid_hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("19s19pEESSWWNBGR")))
        invalid_hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("456m456s456pBBBGG")))
        for hand in invalid_hands:
            self.assertEqual(yaku.CheckHand(hand), False)

    def test_YakuChiitoitsu(self):
        yaku = myf.YakuChiitoitsu()
        hands = []
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("113355m77s99pSSBB")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("1199m1199s11pEERR")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("1199m1199s115599p")))
        for hand in hands:
            self.assertEqual(yaku.CheckHand(hand), True)
        invalid_hands = []
        invalid_hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("111m19s19pESWNBGR")))
        invalid_hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("789m19s19pESWNBGR")))
        invalid_hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("19s19pEESSWWNBGR")))
        invalid_hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("456m456s456pBBBGG")))
        for hand in invalid_hands:
            self.assertEqual(yaku.CheckHand(hand), False)

    def test_YakuSuuankou(self):
        yaku = myf.YakuSuuankou()
        hands = []
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("333m555777s44488p")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("111m777999s11188p")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("555m666sEEEBBBGG")))
        for hand in hands:
            self.assertEqual(yaku.CheckHand(hand), True)
        invalid_hands = []
        invalid_hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("111m19s19pESWNBGR")))
        invalid_hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("789m19s19pESWNBGR")))
        invalid_hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("19s19pEESSWWNBGR")))
        invalid_hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("456m456s456pBBBGG")))
        invalid_hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("333m555789s44488p")))
        invalid_hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("345m123456s444pNN")))
        invalid_hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("123m123s123pEERRR")))
        invalid_hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("333m555777s44489p")))
        for hand in invalid_hands:
            self.assertEqual(yaku.CheckHand(hand), False)

    def test_YakuDaisangen(self):
        yaku = myf.YakuDaisangen()
        hands = []
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("333m55sBBBGGGRRR")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("567s88pBBBGGGRRR")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("66m789pBBBGGGRRR")))
        for hand in hands:
            self.assertEqual(yaku.CheckHand(hand), True)
        invalid_hands = []
        invalid_hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("111m19s19pESWNBGR")))
        invalid_hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("789m19s19pESWNBGR")))
        invalid_hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("19s19pEESSWWNBGR")))
        invalid_hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("456m456s456pBBBGG")))
        invalid_hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("333m555789s44488p")))
        invalid_hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("345m123456s444pNN")))
        invalid_hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("123m123s123pEERRR")))
        invalid_hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("333m555777s44489p")))
        invalid_hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("119m19s19pESWNBGR")))
        invalid_hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("113355m77s99pSSBB")))
        invalid_hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("333m555777s44488p")))
        for hand in invalid_hands:
            self.assertEqual(yaku.CheckHand(hand), False)

    def test_Hand(self):
        hands = []
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("123m123s123pEEESS")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("11122233344455m")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("11122233344455s")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("11122233344455p")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("22345m789s123pWWW")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("23455678s123pEEE")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("EEESSSWWNNNBBB")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("11112345678999p")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("11122345678999p")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("11123345678999p")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("11123445678999p")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("11123455678999p")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("11123456678999p")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("11123456778999p")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("11123456788999p")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("11123456789999p")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("223344556677sGG")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("22334455566677s")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("11222333444555m")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("11122333444555m")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("11122233444555m")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("11122233344555m")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("55556666777788s")))
        hands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("22233344567888s")))
        for hand in hands:
            print(hand.tileCounts)
            print(hand.tileGroups)
            self.assertNotEqual(len(hand.tileGroups), 0)

        horaImpossibleHands = []
        horaImpossibleHands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("2478m111s899pESSR")))
        horaImpossibleHands.append(myf.Hand(self.hnc.ConvertTextToSetNotation("EEESSSWWNBGRRR")))
        for hand in horaImpossibleHands:
            print(hand.tileCounts)
            print(hand.tileGroups)
            self.assertEqual(len(hand.tileGroups), 0)


if __name__ == '__main__':
    unittest.main()
