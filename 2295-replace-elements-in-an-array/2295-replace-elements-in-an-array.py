class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        dictionary = {}
        # index = 0
        
        for index , number in enumerate(nums):
            dictionary[number] = index
       
        for initial , final in operations:
# Locating the index in nums and swapping it
            index = dictionary[initial]
            nums[index] = final
# Creating A new elemnt in the dictionary using the new key ie final value with the previous index
# Deleting the previous elt in dictionary
            dictionary[final] = index
            del dictionary[initial]
        
        return nums
    
    # Time: O(max(len(nums),len(operations)))
#     Space:O(N)
        
        
        
        
        
        
        
        
        
        
        
        
        # # Brute Force
        # for index in range(len(nums)):
        #     for initial , final in operations:
        #         if initial ==  nums[index]:
        #             nums[index] = final
        # return nums