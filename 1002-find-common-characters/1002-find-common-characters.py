class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        word_values = [i for i in words[0]]
        print(word_values)
        result= []
        
        for i in range(1  , len(words)):
            for char in words[i]:
                if char in word_values:
                    result.append(char)
                    word_values.remove(char)
            
            word_values = result
            
            result = []
            
        return word_values