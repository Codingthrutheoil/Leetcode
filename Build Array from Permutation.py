class Solution:
    def buildArray(self, nums):
        nums2 = nums[:]
        i = 0
        for a in nums:
            nums[i] = nums2[a]
            i += 1
        return nums