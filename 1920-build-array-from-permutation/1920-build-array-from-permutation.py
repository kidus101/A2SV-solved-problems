class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        answer = list()
        
        for num in nums:
            answer.append(nums[num])
            
        return answer
    
    # Time:O(N) Space:O(N)