class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dictionary = dict()
        counter = 0
        [1,2,3,1,1,3]

        for num in nums:
            if num in dictionary:
                counter += dictionary[num]
                dictionary[num] += 1
                
            else:
                dictionary[num] = 1
        return counter
        
        # TC:O(N) & sC:O(1)
        
        
        
        
#         N = len(nums)
#         counter = 0
        
#         for i in range(N):
#             for j in range(i+1,N):
#                 if nums[i] == nums[j]:
#                     counter += 1
#         return counter
    
#     #Time complexity = o(n^2)    & SC=O(1)                                                                                                                                                                                                                                                                                                                                                                                                                                              