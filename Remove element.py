class Solution:
    def removeElement(self, nums, val):
        counts = 0
        for values in nums:
            if values != val:
                nums[counts] = values
                counts += 1
        return counts