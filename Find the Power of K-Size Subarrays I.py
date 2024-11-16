class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        pointer1 = 0
        pointer2 = 0 + k
        results = []

        while pointer2 < len(nums)+1:
            nums2 = nums[pointer1:pointer2]
            if all((nums2[a+1] - nums2[a] == 1) for a in range(len(nums2)-1)):
                results.append(nums2[-1])
            else:
                results.append(-1)
            pointer1 += 1
            pointer2 += 1
        return(results)
