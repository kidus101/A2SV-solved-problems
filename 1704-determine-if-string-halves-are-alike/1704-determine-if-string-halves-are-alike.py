class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        print
        a =s[:(n//2)]
        b= s[n//2:]
        
        a_vowel = []
        b_vowel = []
        
        for char in a:
            if char in "aeiouAEIOU":
                a_vowel.append(char)
        
        for char in b:
            if char in "aeiouAEIOU":
                b_vowel.append(char)
        
        if len(a_vowel) == len(b_vowel):
            return True
        else:
            return False