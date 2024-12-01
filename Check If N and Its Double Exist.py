class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for a in range(len(arr)):
            insert = arr[a]
            if a == 0:
                if float(insert) / 2 in arr[1:]:
                    return True
                continue
            else:
                arr.pop(a)
            if float(insert)/2 in arr:
                return True
            arr.insert(a, insert)
        return False
