class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # TC:O(N) & SC:O(N)
        
        ans = []
        dict_ = dict()
        stack_ = []
        
        for num in nums2:
            while stack_ and num > stack_[-1]:
                dict_[stack_.pop()] = num
            
            stack_.append(num)
        
        for num in nums1:
            if num in dict_:
                ans.append(dict_[num])
            else:
                ans.append(-1)
        return ans