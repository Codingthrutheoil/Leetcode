class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        count = 0
        for a in details:
            if int(a[11] + a[12]) > 60:
                count += 1
        return count
