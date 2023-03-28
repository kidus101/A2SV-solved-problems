class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        i = 0
        # min_ = min (nums)
        
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
       
        output = []
        
        for idx in range(len(nums)):
            
            if idx + 1 != nums[idx]:
                output.append(idx + 1)
                
            else:
                continue 
                
        return output
        
        