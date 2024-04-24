class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n in [1, 2]:
            return 1
        t1, t2, t3 = 0, 1, 1
        for a in range(3, n):
            temp = t3
            t3 = t2 + t3 + t1
            t1, t2 = t2, temp
        return t1 + t2 + t3
