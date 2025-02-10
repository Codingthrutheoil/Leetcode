class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        alpha_s = []
        num_s = []

        for a in s:
            if a.isalpha():
                alpha_s.append(a)
            else:
                if len(alpha_s) > 0:
                    alpha_s.pop(-1)
                else:
                    num_s.append(a)
        return(''.join(alpha_s + num_s))
