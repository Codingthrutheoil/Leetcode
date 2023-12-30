class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        checker = {}

        for i in words:
            for a in i:
                if a not in checker.keys():
                    checker[a] = 1
                    continue
                checker[a] += 1
        n = len(words)
        for val in checker.values():
            if val % n != 0:
                return False
        return True