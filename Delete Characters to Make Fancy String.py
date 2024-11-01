class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_s = list(s)
        letters = []
        for a in range(len(s)):
            if s[a] in letters:
                letters.append(a)
            else:
                letters = [s[a]]
            if len(letters) >= 3:
                list_s[a] = ""
        return(''.join(str(a) for a in list_s if a != ""))
