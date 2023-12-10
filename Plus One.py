class Solution(object):
    def plusOne(self, digits):
        digits[-1] += 1
        for i in range(len(digits)-1, 0, -1):
            if digits[i] > 9:
                digits[i-1] += 1
                digits[i] = digits[i] - 10
        if digits[0] > 9:
                digits.insert(0,1)
                digits[1] = digits[1] - 10
        return digits