# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                while head and head.next and fast and fast.next:
                    # if head.next:
                    #     return False
                   
                    
                    if head == fast:
                        return head
                    head = head.next
                    fast = fast.next
                
            
        return None
        