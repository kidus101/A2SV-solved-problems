class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        start = 0
        max_sum = float("-inf")
        
        cur_sum = sum(nums[:k])
        print(cur_sum)
        
        for i in range(k,len(nums)):
            max_sum = max(cur_sum , max_sum)
            cur_sum = cur_sum - nums[start] + nums[i]
            start += 1
            
        max_sum = max(cur_sum , max_sum)
        
        return max_sum / k
        
        
        
        
        
        
#         max_sum = float(-inf)
#         cur_sum = 0
#         start = 0
#         end = 0
        
#         while end   < len(nums):
#             if  end - start + 1 <= k :
#                 cur_sum += nums[end] 
#                 end += 1
                
#             else:
#                 max_sum = max(cur_sum , max_sum)
#                 print(max_sum)
#                 cur_sum = cur_sum - nums[start] + nums[end]
#                 start += 1
#                 end += 1
#         max_sum = max(cur_sum , max_sum)
        
#         return max_sum / k 
        
        
        
        