class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
# ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]

        _dict = defaultdict(list)
    
        for path in paths:
            path = path.split(" ")
            folder = path[0]
            
            for string in path[1:]:
                string = string.split(".txt")
                name = string[0]
                content = string[1]
                _dict[content].append((folder,name))
            
        output = []
        
        for key , value in _dict.items():
            if len(value) > 1:
                temp = []
                for path , name in value:
                    temp.append(path +"/"+ name +".txt")
                    
                output.append(temp)
                
        return output
        
        
        # Time Complecity : O(N*2) 
        # Space Complexity : O(N)
        
        
        
        
        
        
        
                
            