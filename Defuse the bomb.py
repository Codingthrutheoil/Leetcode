class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        code3 = []
        p = len(code)
        if k > 0:
            for a in range(p):
                code4 = 0
                for b in range(abs(k)):
                    code4 += code[(b+a+1)%p]
                code3.append(code4)
        elif k < 0:
            for a in range(p):
                code4 = 0
                for b in range(abs(k),0,-1):
                    code4 += code[a-b]
                code3.append(code4)
        else:
            return([0 for a in range(p)])
        return(code3)
