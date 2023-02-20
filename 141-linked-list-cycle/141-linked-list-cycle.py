# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
#         fast = head
        
#         if head is None:
#             return False
        
#         slow = head.next
#         while slow:
#             slow.
        
#         while  fast and slow:
#             slow = slow.next
#             fast = fast.next.next
            
#             if slow == fast:
#                 return True
    
#         return False
            
#             Fast and slow pointers will land on one node  
        
        set_num = set()
        cur = head
        
        while cur :
            
            if cur not in set_num:
                set_num.add(cur)
                cur = cur.next 
            else:
                return True
    
        return False