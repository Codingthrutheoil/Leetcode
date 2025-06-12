class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = 0

        for a in range(len(nums)-1):
            number1 = abs((nums[a])-(nums[a+1]))
            if number1 > maximum:
                maximum = number1
        number2 = abs((nums[0])-(nums[-1]))
        if number2 > maximum:
            maximum = number2
        return(maximum)
