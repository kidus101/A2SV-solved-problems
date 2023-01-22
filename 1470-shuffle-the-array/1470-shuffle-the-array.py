class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        ptr1 = 0
        ptr2 = n
        ans = list()
        
        while ptr1 < n and ptr2 < len(nums):
            ans.append(nums[ptr1])
            ans.append(nums[ptr2])
            ptr1 += 1
            ptr2 += 1
        return ans