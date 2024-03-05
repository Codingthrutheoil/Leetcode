class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_s = list(s)
        output = len(s)
        while len(list_s) not in [0, 1]:
            if list_s[0] != list_s[-1]:              
                break
            checker = list_s[0] 
            output -= 2
            list_s.pop(0)
            list_s.pop(-1)
            while True:
                if len(list_s) == 0:
                    break
                if len(list_s) == 1:
                    if checker == list_s[0]:
                        list_s.pop(0)
                        output -= 1
                        break
                if not (list_s[0] == checker or list_s[-1] == checker):
                    break
                if list_s[0] == checker:
                    output -= 1
                    list_s.pop(0)
                if list_s[-1] == checker:
                    output -= 1
                    list_s.pop(-1)
        return output
