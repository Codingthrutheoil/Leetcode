class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """
        banned_set = set(banned)
        chosen = 0
        chosen_time = 0
        for a in range(1, n+1):
            if chosen > maxSum:
                break
            if a not in banned_set:
                if chosen + a <= maxSum:
                    chosen += a
                    chosen_time += 1
        return(chosen_time)
