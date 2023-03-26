from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        pre = dummy
        dummy.next = head
        
        while head and head.next:
            if head.val == head.next.val:
                
                while head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
                
            else:
                pre = pre.next
                head = head.next
                
        return dummy.next
    
    #Time:O(n