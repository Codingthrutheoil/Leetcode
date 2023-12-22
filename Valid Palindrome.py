class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1:
            return True
        s = "".join([a.lower() for a in s if a.isalnum()])
        return s == s[::-1] and len(s) >= 0