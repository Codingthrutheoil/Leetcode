class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0
        dictOfLetters = {chr(a):(a-64) for a in range(65, 91)}
        for chrac in columnTitle:
            result = result * 26 + dictOfLetters[chrac]

        return result