class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        i = 0
        
        while i < len(nums):
            j = nums[i]
            if j < len(nums) and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
      
        for idx in range(len(nums)):
            if idx != nums[idx]:
                return (idx)
        
        return len(nums)
        
        
#         output = [ i for i in range(len(nums) + 1)]

#         for num in nums:
#             if num in output:
#                 output.remove(num)
#             else:
#                 continue

#         return  output[0]

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         N = len(nums)
        
#         return ((N) * (N+1) // 2 - sum(nums))
       
# #         total_list = list()
# #         N = len(nums)
        
# #        # [3,0,1]
        
# #         #looping through the max+1 to create the list of total
# #         for i in range(N+1):
# #             total_list.append(i)
            
# #         for i in range(len(nums)):
# #             if (nums[i] in total_list):
# #                 total_list.remove(nums[i])
# #             else:
# #                 return nums[i]
            
# #         return total_list[0] 
        
# #         # TC: O(N) & SC:O(1)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

            
            
            
        