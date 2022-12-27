class Solution:
    def similarPairs(self, words: List[str]) -> int:
        
        N = len(words)
        counter = 0
        
        for i in range(N):
            for j in range(i+1 , N):
                if set(words[i]) == set(words[j]):
                    counter += 1
        return counter
    
    # TIME : O(N^2) and Space:O(1)
        
# iterating through the list and using distnict to create a new array of distnict words By using a set and comapring them

# then comparing the words using the set

 