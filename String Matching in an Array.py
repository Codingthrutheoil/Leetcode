class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        pointer1 = 0
        pointer2 = 1
        len_words = len(words) - 1
        output = []
        while pointer1 != len_words:
            if words[pointer1] in words[pointer2]:
                output.append(words[pointer1])
            elif words[pointer2] in words[pointer1]:
                output.append(words[pointer2])
            pointer2 += 1
            if pointer2 >= len_words+1:
                pointer1 += 1
                pointer2 = pointer1 + 1
        return(list(set(output)))
