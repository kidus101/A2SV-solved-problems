class Solution:
    def simplifyPath(self, path: str) -> str:
        

        list_path = path.split("/")
        stack = []
        
        for element in list_path:
            if element in ["","."]:
                continue
            
            elif element =="..":
                if stack:
                    stack.pop()
            
            else:
                stack.append(element)
                
        return "/" + "/".join(stack)
        
        
        
        
        
        
            