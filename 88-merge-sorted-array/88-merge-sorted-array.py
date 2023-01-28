class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        ptr1 = m - 1
        ptr2 = n - 1
        ptr3 = len(nums1) - 1
        
        
        
        while ptr1 >= 0 and ptr2 >= 0:
            if nums2[ptr2] >= nums1[ptr1]:
                nums1[ptr3] = nums2[ptr2]
                ptr2 -= 1
            else:
                nums1[ptr3] = nums1[ptr1]
                ptr1 -= 1
            ptr3 -= 1 
        
        while ptr2 >= 0:
            nums1[ptr3] = nums2[ptr2]
            ptr2 -= 1
            ptr3 -= 1
        
        return nums1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         class Solution:
#             ptr1, ptr2 = m - 1,  n - 1
#             idx = m + n - 1

#             while ptr1 >= 0 and ptr2 >= 0:
#                 if nums1[ptr1] > nums2[ptr2]:
#                     nums1[idx] = nums1[ptr1]
#                     ptr1 -= 1
#                 else:
#                     nums1[idx] = nums2[ptr2]
#                     ptr2 -= 1
#                 idx -= 1

#             while ptr2 >= 0:
#                 nums1[idx] = nums2[ptr2]
#                 ptr2 -= 1
#                 idx -= 1
        
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# #         ptr1, ptr2 = m - 1,  n - 1
# #         idx = m + n - 1

#         while ptr1 >= 0 and ptr2 >= 0:
#             if nums1[ptr1] > nums2[ptr2]:
#                 nums1[idx] = nums1[ptr1]
#                 ptr1 -= 1
#             else:
#                 nums1[idx] = nums2[ptr2]
#                 ptr2 -= 1
#             idx -= 1

#         while ptr2 >= 0:
#             nums1[idx] = nums2[ptr2]
#             ptr2 -= 1
#             idx -= 1
#         """
      
        