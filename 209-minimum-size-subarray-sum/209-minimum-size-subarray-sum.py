class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # TC:O(N) & SC:O(1)
        left = 0
        window_sum = 0
        min_len = float("inf")
        N = len(nums)
        
        for right in range(N):
            window_sum += nums[right]

            while window_sum >= target:
                min_len = min(min_len , right - left + 1)
                window_sum -= nums[left]
                left += 1
                
        if min_len == float("inf"):
            return 0
        
        return min_len