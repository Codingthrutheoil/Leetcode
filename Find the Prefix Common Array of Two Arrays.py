class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        output = []

        for iteration in range(1, len(A)+1):
            if iteration == 1:
                if A[0] == B[0]:
                    output.append(1)
                else:
                    output.append(0)
                continue
            count = 0
            checked = []
            for backC in range(len(A[:iteration])-1, -1, -1):
                if A[backC] in B[:iteration] and A[backC] not in checked:
                    count += 1
                if A[backC] == B[backC]:
                    checked.append(A[backC])
                    continue
                if B[backC] in A[:iteration] and B[backC] not in checked:
                    count += 1
                checked.append(A[backC])
                checked.append(B[backC])
            output.append(count)
        return(output)
