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
        # Run the RE.match() function to get all match groups.
        pattern = re.compile("([1-9]*m)?([1-9]*s)?([1-9]*p)?([ESWNBGR]*)?")
        matchObj = pattern.match(textNotationStr)
        resultList = [0 for i in range(34)]     # [0, 0, 0, ......, 0] length is 34

        # Is Man tile exist?
        if matchObj.group(1) is not None:
            for v in matchObj.group(1):
                if v >= '1' and v <= '9':
                    resultList[0 + int(v) - 1] += 1 
        # Is Sak tile exist?
        if matchObj.group(2) is not None:
            for v in matchObj.group(2):
                if v >= '1' and v <= '9':
                    resultList[9 + int(v) - 1] += 1 
        # Is Ping tile exist?
        if matchObj.group(3) is not None:
            for v in matchObj.group(3):
                if v >= '1' and v <= '9':
                    resultList[18 + int(v) - 1] += 1 
        # Is East South West North Blank Green Red tile exist?
        if matchObj.group(4) is not None:
            for v in matchObj.group(4):
                if v == 'E':
                    resultList[27] += 1
                elif v == 'S':
                    resultList[28] += 1
                elif v == 'W':
                    resultList[29] += 1
                elif v == 'N':
                    resultList[30] += 1
                elif v == 'B':
                    resultList[31] += 1
                elif v == 'G':
                    resultList[32] += 1
                elif v == 'R':
                    resultList[33] += 1
                else:
                    raise ValueError
        
        # Check the result list and return it as a string.
        if sum(resultList) != 14:
            print("Given hand is not a 14-tile hand.")
            return None
        if len(list(filter(lambda x: x < 0 or x > 4, resultList))) > 0 :
            print("Given hand contains invalid number of tiles.")
            return None
        resultStr = ''.join(["%1d" % x for x in resultList])
        return resultStr

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
