# TC:O(N) & SC:O(1)
# 2 Pointer Solution : Iterating from Left to right until the increase becomes a decrease and 2nd part srarting from right to left increasing doing the same and returning if ( left == right)

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) < 3 :
            return False
        
        left = 0
        right = len(arr)-1
        
        while ( left < len(arr)-2 and arr[left] < arr[left+1]):
            left += 1
        print(left)
        while(right > 1 and arr[right] < arr[right-1]):
            right -= 1
        print(right)
        return left == right
 

# / Using the Maximum no and checking the part ito the right and left

# class Solution:
#     def validMountainArray(self, arr: List[int]) -> bool:
        
#         peek = 0
#         index = 0
        
#         for i in range(len(array)-2):
#             if array[i] > array[i+1]:
#                 peek = array[i]
#                 index = i
        
       
        
        
        
 # Edge Case the array must be didtnict
#         minimum = float("-inf")
#         # dic = enumerate(array)
#         list_ =[]
        
#         peek = 0
#         index = 0
        
#         for i in range(len(array)-2):
#             if array[i] > array[i+1]:
#                 peek = array[i]
#                 index = i
        
#         ptr1 = 0
#         ptr2 = len(array) - 1

#         return True
            