class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # TC:O(N)  SC:O(1)
        
        cur_sum = 0
        output = []
        
        for i in range(len(nums)):
            cur_sum += nums[i]
            output.append(cur_sum)
        
        return output
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # TC:O(N) & sc:o(1)
#         output = []
#         running_sum = 0
        
#         for  i in range(len(nums)):
#             running_sum += nums[i]
#             output.append(running_sum)
        
#         return output