class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        sorted_array = [i+1 for i in range(n)]
        start = 0
        
        while len(sorted_array) > 1:

            loser = (start + k - 1) % len(sorted_array)
            print(start)
            del sorted_array[loser]
            
            if loser <= len(sorted_array):
                start = loser
            else:
                start = 0
        return sorted_array[0]
            
            
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # [1, 2, 3, 4, 5]
        # Using the circular array Formula to rotate 
        
#         initail = 0
        
#         while len(sorted_array) > 1:
#             # ? Use the Modulo formula for circular array
            
#             initial = (initial + k )-1
#             #Before removing the value I have to store the index inorder to know the next value's index meaning 3 for this one
#             sorted_array.remove(sorted_array[initial])
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         sortedN = sorted(i+1 for i in range(n))
        
#         current = len(sortedN)-1
        
#         while len(sortedN)>1:
#             current = (current+k)%len(sortedN)
#             sortedN.remove(sortedN[current])
#             current-=1
#             current%=len(sortedN)

#         return sortedN[0]