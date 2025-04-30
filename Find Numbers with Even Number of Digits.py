class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for a in nums:
            if len(str(a)) % 2 == 0:
                count += 1

        return(count)
