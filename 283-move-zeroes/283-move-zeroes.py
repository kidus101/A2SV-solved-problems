class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        

        # Declaring pointers
        left = 0
        right = 1
        
# Moving 0's to the right keeping in mind that the left pointer explores 0's and the right pointer explores non zeros
    # 0,1,0,3,12
        write = 0
        read = 0

        while read < len(nums):
            if nums[read] != 0:
                temp = nums[read]
                nums[read] = nums[write]
                nums[write] = temp

                write =  write + 1

            read = read + 1
    
        # while right < len(nums):
        #     if nums[left] != 0:
        #         left += 1
        #         right +=1
        #     elif nums[right] == 0:
        #         right +=1
        #     else:
        #         temp = nums[left]
        #         nums[left]=nums[right]
        #         nums[right] = temp
        #         left +=1
        #         right+=1
# Time:O(n) && Space:O(1)








        
        #Brute Force Solution
        # nums = [0,1,0,3,12]
        
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == 0:
        #             nums[i] , nums[j] = nums[j] , nums[i]
                



        
       
        