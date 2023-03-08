class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # TC:O(N) & SC:O(N)
        
        nums = tickets 
        time_taken = 0
		
        minimum_tickeets = nums[k]     
	
        for i in range(len(nums)):   
            
            if k < i and nums[i] >= minimum_tickeets :         
                time_taken += (minimum_tickeets - 1)
                
            elif nums[i] < minimum_tickeets :                   
                time_taken += nums[i]
                
            else:                                            
                time_taken += minimum_tickeets
				
        return time_taken