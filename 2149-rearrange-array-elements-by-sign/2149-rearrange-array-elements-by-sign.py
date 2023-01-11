class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        negative_list = list()
        postive_list = list()
        pivot_list = list()
        output = list()
        
        ptr1 = 0
        ptr2 = len(nums) // 2
        
        for num in nums:
            if num < 0 :
                negative_list.append(num)
            if num >= 0:
                postive_list.append(num)
                   
        final_list = postive_list+negative_list

        while ptr1 < len(postive_list) or ptr2 < len(final_list):
            output.append(final_list[ptr1])
            output.append(final_list[ptr2])
            ptr1 += 1
            ptr2 += 1
        return (output)
    
    # Time: O(N) & Space:O(N)
