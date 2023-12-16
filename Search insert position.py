class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        output = 0
        for i in nums:
            if target <= i:
                break
            output += 1
        return output