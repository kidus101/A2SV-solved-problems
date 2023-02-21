# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        cur = slow
        
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        while prev:
            
            if head.val != prev.val:
                return False

            head = head.next
            prev = prev.next
        return True
        
        
        
        
            
        
        #Time Complexity : O(n)
        #space Complexity: O(1)
        
        #  Asked to Do it using arrays 
        #that is O(n) can be done as follows.
        
#         nums = []
#         while head:
#             nums .append(head.val)
#             head = head. next
            
#         leftptr , rightptr =0 , len(nums) - 1 
        
#         while leftptr < rightptr :
#             if nums[leftptr] != nums[rightptr]:
#                 return False
#             leftptr += 1
#             rightptr-= 1   
#         return True
              
    #Time Complexity : O(n)
        #space Complexity: O(n)
    
        
        
        
        
        
        
        
        
        
        
        
        
 



