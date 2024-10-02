class Solution(object):
    def arrayRankTransform(self, arr):
        arr2 = sorted(list(set(arr)))
        rank = {arr2[a]:a+1 for a in range(len(arr2))}
        return([rank[arr[a]] for a in range(len(arr))])
