class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # TC:O(N) & SC:O(N)
        
        left = 0
        right =len(nums) - 1
        
        while left < right :
            
            if nums[left] + nums[right] < target:
                left += 1
                
            elif nums[left] + nums[right] > target:
                right -= 1
                
            else:
                return (left+1,right+1)
        
            
        
        
        
        
        
        
        
        
        # output = []
        
#         for i in range(len(numbers)):
#             for j in range( len(numbers)):
#                 if numbers[i] + numbers[j] == target:
#                     output.append(i+1)
#                     output.append(j+1)
                    
#         return set(output)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # for idx , num in enumerate(numbers):
        #     if numbers[idx] + num
        #         output.append(idx)
        #         output.append()