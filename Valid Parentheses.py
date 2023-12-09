class Solution(object):
    def isValid(self, s):
        result = False
        for char in range(len(s)):
            if s[char] not in "{([":
                continue
            if s[char] == "(" and s[char+1] == ")" or \
            s[char] == "[" and s[char+1] == "]" or \
            s[char] == "{" and s[char+1] == "}":
                result = True
            else:
                result = False
                continue
        return result