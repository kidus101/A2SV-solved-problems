class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        curr = 0
        stack = []
        
        
        for pos in range(len(s)):
            
            if s[pos] == '(':
                stack.append('(')
                
            else:
                while stack[-1] != '(':
                    curr += stack[-1]
                    stack.pop()
                
                if curr:
                    stack[-1] = curr * 2 
                    
                else:
                     stack[-1] = 1
                    
                curr = 0
                
        return sum(stack)