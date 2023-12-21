class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        output = []
        if numRows >= 1:
            output.append([1])
        if numRows >= 2:
            output.append([1, 1])
        if numRows > 2:
            for i in range(3, numRows+1):
                list_3 = [1]
                for a in range(i-2):
                    list_3.append(output[i-2][a]+output[i-2][a+1])
                list_3.append(1)
                output.append(list_3)
        return output