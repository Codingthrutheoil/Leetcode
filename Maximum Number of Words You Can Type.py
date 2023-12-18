class Solution:
    def canBeTypedWords(self, text, brokenLetters):
        len_of_word = len(text.split())
        brokenLetters = set(brokenLetters)
        for a in text.split():
            for b in a:
                if b in brokenLetters:
                    len_of_word -= 1
                    break
        return len_of_word
