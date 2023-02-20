# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # if not head:
        #     return False
        
        fast = head
        slow = head
 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
    
        return False
            

        
    
    
#     Using A set to check if the Node is already in the set If it's return True
#         set_num = set()
#         cur = head
        
#         while cur :
            
#             if cur not in set_num:
#                 set_num.add(cur)
#                 cur = cur.next 
#             else:
#                 return True
    
#         return False