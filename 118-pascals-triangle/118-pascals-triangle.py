class Solution:
    def generate(self, numrows: int) -> List[List[int]]:

        if numrows == 0:
            retrun [[]]
        
        if numrows == 1:
            return [[1]]
        
        new_row  = [1]
        history = self.generate(numrows-1)
        previous_line = history[-1]
        
        print(previous_line)
       
        for i in range(numrows - 2):
            new_row .append(previous_line[i] + previous_line[i+1])
        
        new_row .append(1)
                           
        return (history + [new_row ])
    
        