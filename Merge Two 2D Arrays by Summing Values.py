class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        nums3 = sorted(nums1 + nums2)

        current_id = nums3[0][0]
        total = nums3[0][1]
        output = [nums3[0]]
        len_nums3 = len(nums3)

        for a in range(1, len_nums3):
            if nums3[a][0] == current_id:
                total += nums3[a][1]
                if a == len_nums3 - 1:
                    output[-1][1] = total
                    break
                continue
            output[-1][1] = total
            output.append(nums3[a])
            total = nums3[a][1]
            current_id = nums3[a][0]

        return(output)
