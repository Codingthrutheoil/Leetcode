class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        one = two = 0
        while one < len(nums1) and two < len(nums2):
            if nums1[one] == nums2[two]:
                return nums1[one]
            elif nums1[one] > nums2[two]:
                two += 1
                continue
            elif nums1[one] < nums2[two]:
                one += 1
                continue
        return -1
