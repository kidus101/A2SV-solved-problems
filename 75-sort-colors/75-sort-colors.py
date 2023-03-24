def counting_sort(nums):
    """
    Sorts the given list of integers in ascending order using counting sort.
    """
    max_num = max(nums)
    count = [0] * (max_num + 1)
    sorted_nums = [0] * len(nums)
    
    # Count the frequency of each number in the list
    for num in nums:
        count[num] += 1
    
    # Calculate the cumulative sum of the count array
    for i in range(1, len(count)):
        count[i] += count[i-1]
    
    # Sort the list in ascending order
    for num in nums:
        index = count[num] - 1
        sorted_nums[index] = num
        count[num] -= 1
    
    return sorted_nums


  # Using Counting Sort  
# 1. knowing the max number
# 2. Creating a counting array of length max_number called count
# 3. Counting in the respective places of the count arra
# 4. Finding the cumulative sum of coun and updating count
# 5.






# def sortColors(self, nums):
#     red, white, blue = 0, 0, len(nums)-1
    
#     while white <= blue:
#         if nums[white] == 0:
#             nums[red], nums[white] = nums[white], nums[red]
#             white += 1
#             red += 1
#         elif nums[white] == 1:
#             white += 1
#         else:
#             nums[white], nums[blue] = nums[blue], nums[white]
#             blue -= 1


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
        


    
 


