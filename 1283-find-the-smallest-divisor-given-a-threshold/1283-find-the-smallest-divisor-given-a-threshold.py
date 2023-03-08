class Solution:
        # TC:O(NlogN) SC:O(N)
        
        def helper(self,nums,m):
            
            Sum = 0
            
            for n in nums:
                Sum += math.ceil(n/m)
                
            return Sum
    
        def smallestDivisor(self, nums: List[int], threshold: int) -> int:

            left = 1
            right = max(nums)

            while left < right:

                mid = (left + right )//2

                Sum = self.helper(nums,mid)

                if Sum > threshold:
                    left = mid + 1

                else:
                    right = mid 

            return right
