class Solution:
    # TC:O(N) & SC:O(1)
    def atMost(self, nums: List[int], k: int) -> int:
        
        total_no_Subarrays = 0
        
        left = 0
        n = len(nums)
        
        no_of_odds = 0
        
        for right in range(n):
            if nums[right] % 2 != 0 :
                no_of_odds += 1
                
            
            while no_of_odds > k:
                if nums[left] % 2 != 0: 
                    no_of_odds -= 1
                left += 1
            
            total_no_Subarrays +=  right - left + 1
            
        
        return total_no_Subarrays

   

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atMost(nums , k) - self.atMost(nums , k-1)