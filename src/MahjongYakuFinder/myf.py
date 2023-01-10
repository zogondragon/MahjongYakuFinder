import re

OrderOfCounts = ["1m", "2m", "3m", "4m", "5m", "6m", "7m", "8m", "9m",
    "1s", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s",
    "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p",
    "E", "S", "W", "N", "B", "G", "R"]

class HandNotationConverter:
    """This class converts between human readable text notation and
    machine readable count notation."""
    def ConvertTextToSetNotation(self, textNotationStr):
        # The text notation should be sorted (m) -> (s) -> (p) -> (ESWNBGR) order.
        if self.VerifyTextNotation(textNotationStr) == False:
            print("Given hand is not a proper hand.")
            return None
        # is Man tile exist?

        # is Sak tile exist?

        # is Ping tile exist?

        # is East South West North Blank Green Red tile exist?

        return "DUMMY RETURN"

    def ConvertSetToTextNotation(self, setNotationStr):
        pass

    def VerifyTextNotation(self, textNotationStr):
        # Check if not allowed character is present in the input string.
        errorpattern = re.compile("[^1-9mspESWNBGR]")
        if errorpattern.match(textNotationStr) is not None:
            return False

        # Check if the input string contains more or less than 14 tiles.
        tileLength = len(textNotationStr.replace('m', '').replace('s', '').replace('p', ''))
        if tileLength != 14:
            return False

        # Check the ordering and count of tiles.
        pattern = re.compile("(1{0,4}2{0,4}3{0,4}4{0,4}5{0,4}6{0,4}7{0,4}8{0,4}9{0,4}m)?"+
                             "(1{0,4}2{0,4}3{0,4}4{0,4}5{0,4}6{0,4}7{0,4}8{0,4}9{0,4}s)?"+
                             "(1{0,4}2{0,4}3{0,4}4{0,4}5{0,4}6{0,4}7{0,4}8{0,4}9{0,4}p)?"+
                             "E{0,4}S{0,4}W{0,4}N{0,4}B{0,4}G{0,4}R{0,4}")
        return True if pattern.fullmatch(textNotationStr) is not None else False

class Hand:
    """Every mahjong hand can be regarded as unordered sets. Every tile of
    same kind is treated indifferently, thus we can just store the counts of
    each kind of tiles for our purpose."""
    pass
