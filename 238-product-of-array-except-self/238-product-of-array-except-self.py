class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # TC:O(N) & SC:O(N)
        
        prefix = [1]*len(nums)
        postfix = [1]*len(nums)
        output = [0]*len(nums)
        
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        print(prefix)    
        for i in range(len(nums)-2 ,-1,-1):
            postfix[i] = postfix[i+1] * nums[i+1] 
        print(postfix)      
        
        i = 0
        while i < len(nums):
            output[i] = postfix[i] * prefix[i]
            i += 1
            
                                                
        return output                                         
                                                    
                                                   
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# 		curProd = 1
# 		result = []

# 		for i in range(len(nums)):
# 			result.append(curProd)
# 			curProd *= nums[i]

# 		curProd = 1

# 		for i in range(len(nums)-1, -1, -1):
# 			result[i] *= curProd
# 			curProd *= nums[i]

# 		return result
        
        
        
        
       
    # Brute force approach
    # Using a nested for loop with i and j where and we muliply each and every j except where i == j. So we skip the elemnt we are on at
    
#         answer = []
        
#         for i in range(n):
#             product = 1
#             for j in range(n):
#                 if i == j : continue
#                 product *= nums[j]
#             answer.append(product)
#         return answer
        
# Using Time: O(N) and Space:O(N)
       
        