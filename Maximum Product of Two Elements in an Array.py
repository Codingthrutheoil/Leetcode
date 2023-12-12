class Solution(object):
    def maxProduct(self, nums):
        i = max(nums)
        del nums[nums.index(i)]
        j = max(nums)
        return  ((i-1)*(j-1))