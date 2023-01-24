
  # Using Counting Sort  
# 1. knowing the max number
# 2. Creating a counting array of length max_number called count
# 3. Counting in the respective places of the count arra
# 4. Finding the cumulative sum of coun and updating count
# 5.

class Solution:
    def sortColors(self, array: List[int]) -> None:

        size = len(array)
        output = [0] * size

        count = [0] * 10

        for i in range(0, size):
            count[array[i]] += 1


        for i in range(1, 10):
            count[i] += count[i - 1]

        i = size - 1
        while i >= 0:
            output[count[array[i]] - 1] = array[i]
            count[array[i]] -= 1
            i -= 1

        for i in range(0, size):
            array[i] = output[i]

        return array

    # class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         Time:O(N^2) Bubble Sort
#         for i in range(len(nums)):
#             for j in range(len(nums)-1):
#                 if nums[j] > nums[j+1]:
#                     nums[j] , nums[j+1] = nums[j+1] , nums[j]
                    
#         return nums


        
        
        
        
        
        
#         for i in range(len(nums)):
            
#             for j in range(0, len(nums) - i - 1):
                
#                 if nums[j] > nums[j + 1]:
#                     temp = nums[j]
#                     nums[j] = nums[j+1]
#                     nums[j+1] = temp
        
#         return nums
        


    
 


