class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        pattern0 = 0
        pattern1 = 0

        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == "0":
                    pattern1 += 1
                else:
                    pattern0 += 1
            else:
                if s[i] == "1":
                    pattern1 += 1
                else:
                    pattern0 += 1
        return min(pattern0, pattern1)
