class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        num1 = 0
        num2 = 0

        for a in range(n+1):
            if a % m == 0:
                num2 += a
            else:
                num1 += a
        return(num1-num2)
