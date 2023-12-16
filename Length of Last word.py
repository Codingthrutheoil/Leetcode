class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        while '  ' in s:
            s = s.replace('  ', ' ')
        s = s.split(" ")
        for i in s:
            if i == "":
                s.remove("")
        return len(s[-1])