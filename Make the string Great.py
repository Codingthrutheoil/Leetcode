class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        list_s = list(s)
        pointer1, pointer2 = 0, 1
        checker = True

        while checker:
            if pointer2 == len(list_s) or len(list_s) == 0:
                break
            if (((list_s[pointer1].isupper() and list_s[pointer2].islower())
                and list_s[pointer1].lower() == list_s[pointer2].lower())
                    or ((list_s[pointer1].islower() and list_s[pointer2].isupper())
                        and list_s[pointer1].lower() == list_s[pointer2].lower())):
                list_s.pop(pointer2)
                list_s.pop(pointer1)
                pointer1, pointer2 = 0, 1
                continue
            pointer1 += 1
            pointer2 += 1
            if pointer2 == len(list_s) or len(list_s) == 0:
                checker = False
        return "".join(list_s)
