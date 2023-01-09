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
            print("Given hand is not well-ordered.")
            return None
        # is Man tile exist?

        # is Sak tile exist?

        # is Ping tile exist?

        # is East South West North Blank Green Red tile exist?

        return "DUMMY RETURN"

    def ConvertSetToTextNotation(self, setNotationStr):
        pass

    def VerifyTextNotation(self, textNotationStr):
        pass

class Hand:
    """Every mahjong hand can be regarded as unordered sets. Every tile of
    same kind is treated indifferently, thus we can just store the counts of
    each kind of tiles for our purpose."""
    pass
