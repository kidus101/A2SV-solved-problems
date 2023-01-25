class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # TC:O(N) & SC:O(1)
        k %= len(nums)
        
        ptr1 = 0
        ptr2 = k - 1
        ptr3 = len(nums) - 1  
        
        
        N = len(nums)
        # nums.reverse()
        
        def reverse_array(ptr1 , ptr2):
            while ptr1 < ptr2 :
                nums[ptr1] , nums[ptr2] = nums[ptr2] , nums[ptr1]
                ptr1 += 1
                ptr2 -= 1
        
        
        reverse_array(0,N-1)
        reverse_array(0,k-1)
        reverse_array(k,N-1)
        
#         ptr4 = k 
        
#         while ptr4 < ptr3:
#             nums[ptr4] , nums[ptr3] = nums[ptr3] , nums[ptr4]
#             ptr4 += 1
#             ptr3 -= 1
       
#         print(nums)
            
        
       
        
        
        
#         ptr1 = 0
#         ptr2 = len(nums) - k
#         output = [0] * len(nums)
#         k = k%len(nums)
        
        
#         # if len(nums) < k :
#         #     return nums[::-1]
        
#         for i in range(len(nums) - k , len(nums)):
#             output.append(nums[i])
      
        
#         for i in range(0,ptr2):
#             output.append(nums[i])
        
#         for i in range(len(nums)):
#             nums[i] = output[i]
    
#         return nums

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#         def reverse(nums , left , right):
#             while(left < right):
#                 nums[left] , nums[right] = nums[right], nums[left] 
#                 left += 1
#                 right -= 1
#         k  = k % len(nums)
#         reverse(nums,0,len(nums)-1)
#         reverse(nums,0,k-1)
#         reverse(nums,k,len(nums)-1)
        
#         # Time: O(1)
#         # Space:O(1)
       
      
        
        