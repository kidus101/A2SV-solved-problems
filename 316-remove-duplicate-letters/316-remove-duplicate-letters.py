class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        stack = []
        visited = set()
        last_occurance = {}
        
        for i in range(len(s)):
            last_occurance[ s[i] ] = i
        
        
        for idx, char in enumerate(s):
            if( char in visited ):
                continue
                
            
                
            while( stack and stack[-1] > char and last_occurance[stack[-1]] > idx ):

                removed_character = stack.pop()
                visited.remove(removed_character)

            visited.add(char)
            stack.append(char)
                
            
        return ''.join(stack)