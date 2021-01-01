class PatternSearch:

    def __init__(self, str , patt):
        self.str = str
        self.patt = patt
    def patterSearch(self):
        patternLength = len(self.patt)
        stringLength = len(self.str)
        lenDiff = stringLength - patternLength
        if stringLength < patternLength:
            return -1
        for i in range(lenDiff + 1):
            j = 0
            for j in range(0,patternLength):
                if self.str[i+j] != self.patt[j]:
                    break
            if j == patternLength - 1:
                print("Pattern found at "+str(i))





T = "UPGRADEDUBUPGRAABUPGRADEDU"

P = "UPGRAD"
sample = PatternSearch(T, P)
sample.patterSearch()