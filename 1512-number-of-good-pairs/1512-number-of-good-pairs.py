class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        N = len(nums)
        counter = 0
        
        for i in range(N):
            for j in range(i+1,N):
                if nums[i] == nums[j]:
                    counter += 1
        return counter
    
    #Time complexity = o(n^2)    & SC=O(1)                                                                                                                                                                                                                                                                                                                                                                                                                                              