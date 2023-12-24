class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        setofnums = set(nums)
        dictofnums = {}
        for a in setofnums:
            dictofnums[a] = nums.count(a)
        for b in dictofnums.keys():
            if dictofnums[b] > len(nums)/2:
                return b