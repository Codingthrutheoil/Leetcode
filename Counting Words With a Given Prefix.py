class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        output = 0
        len_pref = len(pref)
        for a in words:
            if pref in a[:len_pref]:
                output += 1
        return output
