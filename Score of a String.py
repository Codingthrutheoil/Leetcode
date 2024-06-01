class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        output_s = []
        for a in range(len(s)-1):
            output_s.append(abs(ord(s[a])-ord(s[a+1])))
        return sum(output_s)
