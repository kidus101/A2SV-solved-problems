class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        # TC:O(N) & SC:O(N)
        
        output = []
        sorted_num = sorted(nums)
        
        for num in nums:
            output.append(sorted_num.index(num))
        
        return output
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         array = []
        
#         for i in range (len(nums)):
#             count = 0
#             for j in range (1, len(nums)):
#                 if nums[j] < nums[i]:
#                     count +=1
#             array.append(count)
            
#         return array







# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

#         temp = sorted(nums)
#         mapping = {}
#         result = []
#         for i in range(len(temp)):
#             if temp[i] not in mapping:
#                 mapping[temp[i]] = i
#         print(mapping)
#         for i in range(len(nums)):
#             result.append(mapping[nums[i]])
#         print(result)
        
#         return result