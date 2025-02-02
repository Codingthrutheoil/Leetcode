class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_sorted = sorted(nums)

        for a in range(len(nums), 0, -1 ):
            if nums_sorted == nums[a:] + nums[:a]:
                return(True)
        return(False)
