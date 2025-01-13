class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_s = [s.count(a) for a in set(s)]
        ans = 0
        for b in count_s:
            if b < 2: continue
            if b > 2 and b % 2 == 1:
                ans += (b // 2) * 2
            elif b > 2 and b % 2 == 0:
                ans += ((b-2) // 2) * 2
        return(len(s) - ans)
