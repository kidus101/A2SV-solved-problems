class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        palindrome_string = ""
        
        for word in words:
            if word == word[::-1]:
                return word
        
        
        
        
        return palindrome_string