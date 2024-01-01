class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        content = 0
        s.sort()
        g.sort()
        cookie_test = len(s) - 1
        child_test = len(g) - 1
        while cookie_test >= 0 and child_test >= 0:
            if s[cookie_test] >= g[child_test]:
                content += 1
                cookie_test -= 1
                child_test -= 1
            else:
                child_test -= 1

        return content
