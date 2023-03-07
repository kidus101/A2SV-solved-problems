class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # TC:O(N) SC:O(N)
            stack = [] 
            output = [-1] * len(nums)
            
            for idx, num in enumerate(nums):  

                while stack and nums[stack[-1]] < num:
                    output[stack.pop()] = num

                stack.append(idx)

            for idx, num in enumerate(nums):      

                while stack and nums[stack[-1]] < num:
                    output[stack.pop()] = num

            return output
