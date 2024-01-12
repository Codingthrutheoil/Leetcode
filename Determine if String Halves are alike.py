class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        len_string = len(s)
        count1 = count2 = 0
        for a in s[:len_string//2]:
            if a.lower() in ["a", "e", "i", "o", "u"]:
                count1 += 1
        for b in s[len_string//2:]:
            if b.lower() in ["a", "e", "i", "o", "u"]:
                count2 += 1
        return count1 == count2