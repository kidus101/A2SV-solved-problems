class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        #check if nums[i] == nums[i+1] 
        # if yes do operations else both incerement by 1
        #After the array is finished we move the zeros to the last 
        
        i = 0
        
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            i += 1

            
        left = 0
        right = 1
        
        while right < len(nums):
            if nums[left] != 0:
                left += 1
                right +=1
            elif nums[right] == 0:
                right +=1
            else:
                temp = nums[left]
                nums[left]=nums[right]
                nums[right] = temp
                left +=1
                right+=1

        return nums
    
    # Time:O(N) & Space:O(1)
      
            