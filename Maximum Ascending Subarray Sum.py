class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sub_arrays = []
        counter = [nums[0]]
        for a in range(1, len(nums)):
            if counter[-1] < nums[a]:
                counter.append(nums[a])
            else:
                sub_arrays.append(sum(counter))
                counter = [nums[a]]
        sub_arrays.append(sum(counter))

        return(max(sub_arrays))
