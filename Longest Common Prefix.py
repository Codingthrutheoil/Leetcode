class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        CommonPrefix = strs[0]
        for word in strs[1:]:
            while word.find(CommonPrefix) != 0:
                CommonPrefix = CommonPrefix[:-1]
                if not CommonPrefix:
                    return ""
        return CommonPrefix