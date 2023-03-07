class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def atMost(goal):
            
            if goal < 0:
                return 0
            
            answer = 0
            left = 0
            
            for right in range(len(nums)):
                
                goal -= nums[right]
                
                while goal < 0:
                    goal += nums[left]
                    left += 1
                    
                answer += right - left + 1
                
            return answer
        
        return atMost(goal) - atMost(goal - 1)