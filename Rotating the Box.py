class Solution(object):
    def rotateTheBox(self, box):
        """
        :type box: List[List[str]]
        :rtype: List[List[str]]
        """
        length = len(box[0])
        for a in box:
            for b in range(len(a)-1, 0, -1):
                if a[b] == "." and a[b-1] == "#":
                    a[b], a[b-1], c = "#", ".", 1
                    while b+c <= length-1:
                        if a[b + c] == ".":
                            a[b + c], a[b + c - 1] = "#", "."
                        else:
                            break
                        c += 1

        box = list(reversed(box))
        box2 = [[row[i] for row in box] for i in range(len(box[0]))]
        return(box2)
