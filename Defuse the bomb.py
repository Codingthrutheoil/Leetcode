def iterOfK(startnumber, kvalue, length):
    if kvalue < 0:
        kvalue = abs(kvalue)
        iter_of_k = [startnumber - 1 if startnumber not in [0, length] else length - 1]
        for a in range(1, kvalue):
            iter_of_k.append((iter_of_k[0] - a) % length)
        return iter_of_k
    iter_of_k = [(startnumber + 1) % length]
    for a in range(1, kvalue-1):
        iter_of_k.append((iter_of_k[0]+a) % length)
    iter_of_k.append((iter_of_k[-1] + 1) % length)
    return iter_of_k

class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        code_return = [0 for a in code]
        if k == 0:
            return code_return
        if k == 1:
            for a in range(len(code)-1):
                code_return[a] = code[a+1]
            code_return[-1] = code[0]
            return code_return
        len_of_k = len(code)
        for a in range(len(code)):
            iter_of_k = iterOfK(a, k, len_of_k)
            for b in iter_of_k:
                code_return[a] = code_return[a] + code[b]
        return code_return 