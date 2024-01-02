class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        dic_of_nums = {}
        for a in nums:
            if a not in dic_of_nums.keys():
                dic_of_nums[a] = 1
            else:
                dic_of_nums[a] += 1
        nums = []
        inserting_nums = []
        value_checker = 1
        while value_checker != max(dic_of_nums.values()) + 1:
            for key, value in dic_of_nums.items():
                if value_checker <= value:
                    inserting_nums.append(key)
            nums.append(inserting_nums)
            inserting_nums = []
            value_checker += 1
        return nums