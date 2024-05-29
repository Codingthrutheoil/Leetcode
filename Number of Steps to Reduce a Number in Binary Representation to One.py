class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        s, count = int(s,2), 0
        while s != 1:
            count += 1
            if s % 2 == 0:
                s /= 2
            else:
                s += 1
        return count
