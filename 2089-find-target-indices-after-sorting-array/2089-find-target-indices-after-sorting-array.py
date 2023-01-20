class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # TC:O(N) & SC:O(N)
        
        nums.sort()
        output = []
        
        print(enumerate(nums))
        for idx , num in enumerate(nums):
            if num == target:
                output.append(idx)
        
        return output
        
                
        
#             nums.sort()
#             output = []

#             for i in range (len(nums)):
#                 if nums[i] == target:
#                     output.append(i)

#             return output    