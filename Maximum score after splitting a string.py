class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_score = max_iter = 0
        for i in range(len(s)-1):
            max_iter = (s[0:i+1]).count("0") + (s[i+1:len(s)]).count("1")
            max_score = max(max_score, max_iter)
        return max_score