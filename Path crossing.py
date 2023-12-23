class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        all_paths = []
        origin = [0, 0]
        for a in path:
            all_paths.append(origin[:])
            if a == "N":
                origin[0] += 1
            elif a == "S":
                origin[0] -= 1
            elif a == "E":
                origin[1] += 1
            elif a == "W":
                origin[1] -= 1
            if origin in all_paths:
                return True