class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        for a in range(k):
            min_nums = min(nums)
            nums[nums.index(min_nums)] = min_nums * multiplier
        return(nums)
