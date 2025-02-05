class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if sorted(s1) != sorted(s2):
            return False
        counter = 0
        for a in range(len(s1)):
            if s1[a] != s2[a]:
                counter += 1
            if counter > 2:
                return False
        return True
