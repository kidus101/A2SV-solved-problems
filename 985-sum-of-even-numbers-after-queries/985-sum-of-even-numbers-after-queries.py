class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        output = []
        even_sum = 0
        
        for num in nums:
            if(num % 2 == 0):
                even_sum += num
        
        for value ,index in queries:
            if nums[index] % 2 == 0:
                even_sum -= nums[index]
            
            nums[index] += value
            
            if (nums[index] % 2 == 0):
                even_sum += nums[index]
    
            output.append(even_sum)
        
        return output
        
# Time:O(N+M) & Space: O(N)
        
        
        
        
        
        
        
        
#         # Brute Force
        
#         answer = list()
#         nums_copy = nums.copy()
#         print(nums_copy)
        
        
#         for value , index in queries:
#             nums[index] = nums[index] + value
#             new_sum = 0
#         for num in nums:
#             if num % 2 == 0:
#                 new_sum = new_sum + num
#             else:
#                 continue
            
#             answer.append(new_sum)
#         return answer
    
#     # Time:O(N^2) & Space:O(N)