class Solution(object):
    global nums
    def removeDuplicates(self, nums):
        Uindex = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[Uindex] = nums[i]
                Uindex += 1
        return Uindex

