class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        if sentence[0] != sentence[-1]:
            return False
        sentence_list = sentence.split()
        if len(sentence_list) == 1:
            return True
        for a in range(len(sentence_list)-1):
            if sentence_list[a][-1] != sentence_list[a+1][0]:
                return False
        return True
