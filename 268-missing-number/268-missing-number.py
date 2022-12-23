class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        _max = max(nums)
        dic = dict()
        total_list = list()
        result = ""
        N = len(nums)
        
       # [3,0,1]
        
        #looping through the max+1 to create the list of total
        for i in range(N+1):
            total_list.append(i)
        print(total_list)
            
        for i in range(len(nums)):
            if (nums[i] in total_list):
                total_list.remove(nums[i])
            else:
                return nums[i]
        return total_list[0] 
        
        # TC: O(N) & SC:O(1)
            
        # print(dic)
        
#         for index,value in range(len(total_list)):
            
#             for k in range(len(nums)):
#                 if nums[k] in total_list
        
        # for j  in range(total_list):
            
            
            
        