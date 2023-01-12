import collections
import copy
import re

OrderOfCounts = ["1m", "2m", "3m", "4m", "5m", "6m", "7m", "8m", "9m",
    "1s", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s",
    "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p",
    "E", "S", "W", "N", "B", "G", "R"]

TileIndexDict = {"1m": 0, "2m": 1, "3m": 2, "4m": 3, "5m": 4, "6m": 5, "7m": 6, "8m": 7, "9m": 8,
    "1s": 9, "2s": 10, "3s": 11, "4s": 12, "5s": 13, "6s": 14, "7s": 15, "8s": 16, "9s": 17,
    "1p": 18, "2p": 19, "3p": 20, "4p": 21, "5p": 22, "6p": 23, "7p": 24, "8p": 25, "9p": 26,
    "E": 27, "S": 28, "W": 29, "N": 30, "B": 31, "G": 32, "R": 33}

TileGroupCursor = [(1, "man"), (2, "man"), (3, "man"), (4, "man"), (5, "man"), (6, "man"), (7, "man"), (8, "man"), (9, "man"),
    (1, "sak"), (2, "sak"), (3, "sak"), (4, "sak"), (5, "sak"), (6, "sak"), (7, "sak"), (8, "sak"), (9, "sak"),
    (1, "ping"), (2, "ping"), (3, "ping"), (4, "ping"), (5, "ping"), (6, "ping"), (7, "ping"), (8, "ping"), (9, "ping"),
    (0, "E"), (0, "S"), (0, "W"), (0, "N"), (0, "B"), (0, "G"), (0, "R")]

def TextToTileSetNotation(textNotationStr):
    """This function is not confined to 14-tile hand. It can convert any length of tile set."""
    # Check if not allowed character is present in the input string.
    errorpattern = re.compile("[^1-9mspESWNBGR]")
    if errorpattern.search(textNotationStr) is not None:
        return None
    
    # Check the ordering and count of tiles.
    pattern = re.compile("(1{0,4}2{0,4}3{0,4}4{0,4}5{0,4}6{0,4}7{0,4}8{0,4}9{0,4}m)?"+
                         "(1{0,4}2{0,4}3{0,4}4{0,4}5{0,4}6{0,4}7{0,4}8{0,4}9{0,4}s)?"+
                         "(1{0,4}2{0,4}3{0,4}4{0,4}5{0,4}6{0,4}7{0,4}8{0,4}9{0,4}p)?"+
                         "E{0,4}S{0,4}W{0,4}N{0,4}B{0,4}G{0,4}R{0,4}")
    if pattern.fullmatch(textNotationStr) is None:
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
    resultStr = ''.join(["%1d" % x for x in resultList])
    return resultStr

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
        manTileExist = False
        sakTileExist = False
        pingTileExist = False
        manStrList = []
        sakStrList = []
        pingStrList = []
        honorStrList = []
        resultStrList = []

        if len(setNotationStr) != 34:
            print("Given set notation length is not 34.")
            return None
        if setNotationStr.isnumeric() == False:
            print("Given set notation contains non-numeric character.")
            return None
        for i, v in enumerate(setNotationStr):
            if i >= 0 and i < 9 and int(v) > 0:
                manTileExist = True
                manStrList.append(str(i+1) * int(v))
            elif i >= 9 and i < 18 and int(v) > 0:
                sakTileExist = True
                sakStrList.append(str(i-8) * int(v))
            elif i >= 18 and i < 27 and int(v) >0:
                pingTileExist = True
                pingStrList.append(str(i-17) * int(v))
            elif i == 27 and int(v) > 0:
                honorStrList.append(str('E' * int(v)))
            elif i == 28 and int(v) > 0:
                honorStrList.append(str('S' * int(v)))
            elif i == 29 and int(v) > 0:
                honorStrList.append(str('W' * int(v)))
            elif i == 30 and int(v) > 0:
                honorStrList.append(str('N' * int(v)))
            elif i == 31 and int(v) > 0:
                honorStrList.append(str('B' * int(v)))
            elif i == 32 and int(v) > 0:
                honorStrList.append(str('G' * int(v)))
            elif i == 33 and int(v) > 0:
                honorStrList.append(str('R' * int(v)))
            elif i >= 34:
                print("Given set notation is not a proper notation.")
                return None
        
        if manTileExist == True:
            resultStrList.append(''.join(manStrList) + "m")
        if sakTileExist == True:
            resultStrList.append(''.join(sakStrList) + "s")
        if pingTileExist == True:
            resultStrList.append(''.join(pingStrList) + "p")
        resultStrList.append(''.join(honorStrList))
        resultStr = ''.join(resultStrList)
        if self.VerifyTextNotation(resultStr) == False:
            print("Given hand is not a proper hand.")
            return None
        return resultStr

    def VerifyTextNotation(self, textNotationStr):
        # Check if not allowed character is present in the input string.
        errorpattern = re.compile("[^1-9mspESWNBGR]")
        if errorpattern.search(textNotationStr) is not None:
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
    def __init__(self, setNotationStr):
        self.tileCounts = [0 for x in OrderOfCounts]
        if len(setNotationStr) != 34:
            print("Given set notation length is not 34.")
            raise ValueError
        if setNotationStr.isnumeric() == False:
            print("Given set notation contains non-numeric character.")
            raise ValueError
        for i, v in enumerate(setNotationStr):
            if int(v) < 0 or int(v) > 4:
                raise ValueError
            self.tileCounts[i] = int(v)
        if sum(self.tileCounts) != 14:
            print("Given set notation is not 14-tile hand.")
            raise ValueError
        
        # There can be multiple tilegroup interpretations of a given hand, differing Han numbers.
        # Syuntsu is always notated by the starting number. Ex: 123m = 1 m syuntsu, 789p = 7 p syuntsu.
        self.tileGroups = []    # ex: a tileGroup = [ (1, "man", "syuntsu"), (3, "sak", "kotsu"), 
                                # (5, "man", "kotsu"), (6, "ping", "syuntsu"), (0, "E", "toitsu") ] 
        self.FindTileGroups()       # Find and set above variables.

    def ContainsTiles(self, setNotationStr):
        """It returns True when the hand contains given tile set, False when the hand doesn't contain
        given tile set."""
        if len(setNotationStr) != 34:
            print("Given tile set notation length is not 34.")
            raise ValueError
        if setNotationStr.isnumeric() == False:
            print("Given tile set notation contains non-numeric character.")
            raise ValueError
        for i, v in enumerate(setNotationStr):
            if int(v) < 0 or int(v) > 4:
                raise ValueError
            if self.tileCounts[i] - int(v) < 0:
                return False
        return True 

    def DoesntContainTiles(self, setNotationStr):
        """It returns True when the hand doesn't contain any one of given tile set."""
        pass

    def FindTileGroups(self):
        """It finds all 4 mentsu (both syuntsu and kotsu) and 1 toitsu and remember those."""
        # Use backtracking pattern to solve this Constraint Satisfaction Problem.                                
        # Ref: [1] https://en.wikipedia.org/wiki/Backtracking
        #      [2] https://en.wikipedia.org/wiki/Constraint_satisfaction_problem
        # Making difficulty is kotsu > toitsu > syuntsu order, thus find tileGroups in this order.
        cursor = 0
        remainingTileset = copy.deepcopy(self.tileCounts)
        self.BacktrackHelperFindTileGroups(cursor, len(remainingTileset), remainingTileset, [])

    def BacktrackHelperFindTileGroups(self, cursor, end, remainingTileset, tileGroup):
        if sum(remainingTileset) == 0:
            # All tiles visited.
            dc_tileGroup = copy.deepcopy(tileGroup)
            if self.BacktrackHelperVerifyTileGroup(dc_tileGroup) == True:
                # If found temporary solution is verified, then add it to the solutions list.
                # But, do not register duplicated solution.
                isDuplicatedSolution = False
                for solution in self.tileGroups:
                    if collections.Counter(solution) == collections.Counter(dc_tileGroup):
                        isDuplicatedSolution = True
                
                if isDuplicatedSolution == False:
                    self.tileGroups.append(dc_tileGroup)
                return
        if cursor == end:
            return
        if remainingTileset[cursor] == 0:
            self.BacktrackHelperFindTileGroups(cursor+1, end, remainingTileset, tileGroup)
        if remainingTileset[cursor] >= 3:
            # Is this cursor imply a kotsu?
            dc_remainingTileset = copy.deepcopy(remainingTileset)
            dc_tileGroup = copy.deepcopy(tileGroup)
            tileSubgroup = TileGroupCursor[cursor]
            dc_tileGroup.append((tileSubgroup[0], tileSubgroup[1], "kotsu"))
            dc_remainingTileset[cursor] -= 3
            self.BacktrackHelperFindTileGroups(cursor, end, dc_remainingTileset, dc_tileGroup)
        if remainingTileset[cursor] >= 2:
            # Is this cursor imply a toitsu?
            dc_remainingTileset = copy.deepcopy(remainingTileset)
            dc_tileGroup = copy.deepcopy(tileGroup)
            tileSubgroup = TileGroupCursor[cursor]
            dc_tileGroup.append((tileSubgroup[0], tileSubgroup[1], "toitsu"))
            dc_remainingTileset[cursor] -= 2
            self.BacktrackHelperFindTileGroups(cursor, end, dc_remainingTileset, dc_tileGroup)
        if remainingTileset[cursor] >= 1: 
            # Is this cursor imply a syuntsu?
            tileSubgroup = TileGroupCursor[cursor]
            if tileSubgroup[0] >= 1 and tileSubgroup[0] <= 7 and\
               remainingTileset[cursor+1] >= 1 and remainingTileset[cursor+2] >= 1:
                dc_remainingTileset = copy.deepcopy(remainingTileset)
                dc_tileGroup = copy.deepcopy(tileGroup)
                dc_tileGroup.append((tileSubgroup[0], tileSubgroup[1], "syuntsu"))
                dc_remainingTileset[cursor] -= 1
                dc_remainingTileset[cursor+1] -= 1
                dc_remainingTileset[cursor+2] -= 1
                self.BacktrackHelperFindTileGroups(cursor, end, dc_remainingTileset, dc_tileGroup)

    def BacktrackHelperVerifyTileGroup(self, tileGroup):
        mentsuCount = 0
        toitsuCount = 0
        if len(tileGroup) != 5:
            return False
        for v in tileGroup:
            if v[2] == "syuntsu" or v[2] == "kotsu":
                mentsuCount += 1
            elif v[2] == "toitsu":
                toitsuCount += 1
        return True if mentsuCount == 4 and toitsuCount == 1 else False


class AgariConditionBaseClass:
    pass

class YakuBaseClass:
    def __init__(self):
        self.han = 0
        self.isYakuman = False
        self.isHoraPossible = False
    def CheckHand(self, hand):
        pass

class YakuKokushimusou(YakuBaseClass):
    def __init__(self):
        self.han = 13
        self.isYakuman = True
        self.isHoraPossible = True  # Kokushimusou hand can agari(=hora) itself.
    def CheckHand(self, hand):
        condition = TextToTileSetNotation("19m19s19pESWNBGR")   # 13 tile condition
        return hand.ContainsTiles(condition)

class YakuChiitoitsu(YakuBaseClass):
    def __init__(self):
        self.han = 2
        self.isHoraPossible = True  # Chiitoitsu hand can agari(=hora) itself.
    def CheckHand(self, hand):
        return True if len(list(filter(lambda x: x == 2, hand.tileCounts))) == 7\
                    else False

class YakuSuuankou(YakuBaseClass):
    def __init__(self):
        self.han = 13
        self.isYakuman = True
    def CheckHand(self, hand):
        if len(hand.tileGroups) == 0:
            self.isHoraPossible = False
            return False
        else:
            for solution in hand.tileGroups:
                # TODO: Currently, it is returning True if only one of tileGroups satisfy.
                #       Later, the decision for each tileGroup might be needed.
                kotsuCount = 0
                for v in solution:
                    # TODO: Ankou or Minkou decision -- later. I have to implement
                    #       Chi, Pon, Kan first.
                    if v[2] == "kotsu":
                        kotsuCount += 1
                if kotsuCount == 4:
                    return True
            return False
