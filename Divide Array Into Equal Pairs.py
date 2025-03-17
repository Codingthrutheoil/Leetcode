class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for a in set(nums):
            if nums.count(a) % 2 != 0:
                return(False)
        return(True)
