class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        if word.isupper():
            return True
        elif word.islower():
            return True
        elif word[0].isupper():
            if word[1:].islower():
                return True
        return False
        
