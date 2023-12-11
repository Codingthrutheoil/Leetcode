class Solution(object):
    def findSpecialInteger(self, arr):
        Cdict = {}
        highest = 0
        for i in arr:
            if i not in Cdict:
                Cdict[i] = 1
            else:
                Cdict[i] += 1
        highest = (max(Cdict.values()))
        highest = [i for i in Cdict if Cdict[i]==highest]
        highest = highest[0]
        return highest
