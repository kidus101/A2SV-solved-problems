class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        numbers = list()
        middle,left,right = 0,0,0
        
        if num % 3 == 0:
            middle = int(num / 3)
            left = middle - 1
            right = middle + 1
            
        if middle + left + right  == num:
            numbers.append(left)
            numbers.append(middle)            
            numbers.append(right)            
            
        return numbers    
        
        # Time Complexity:O(1) 
        # Space Complexity :O(N)