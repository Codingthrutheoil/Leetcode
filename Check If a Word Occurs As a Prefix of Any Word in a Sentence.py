class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        sentence_list = sentence.split(" ")
        for a in range(len(sentence_list)):
            if searchWord in sentence_list[a] and sentence_list[a].index(searchWord) == 0:
                return(a+1)
        return(-1)
