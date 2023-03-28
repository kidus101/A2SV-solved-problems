class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        
        while i < len(nums):
            j =  nums[i] - 1
            
            if nums[i] != nums[j]:
                nums[i] , nums[j] = nums[j] , nums[i]
            else:
                i += 1
                
        output = [] 
        
        for i in range(len(nums)):
            if i+1 != nums[i]:
                output.append(nums[i])
        
        return output