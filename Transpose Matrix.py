class Solution:
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        transpose_list = []
        transpose = []

        for lst in range(len(matrix[0])):
            for lst2 in range(len(matrix)):
                transpose_list.append(matrix[lst2][lst])
            transpose.append(transpose_list)
            transpose_list = []
        return transpose

a = Solution()
print(a.transpose([[1,2,3],[4,5,6],[7,8,9]]))