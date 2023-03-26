# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return head
        
#         Finding the length of the LL 
        
        tail = head
        length_LL = 1
        
        while tail.next:
            tail = tail.next
            length_LL += 1
        
        k = k % length_LL
        
        if k == 0:
            return head
        
#       knowuing where to cut the linkedlist
        
        cur = head
        
        for i in range(length_LL  - k -1):
            cur = cur.next
        
        new_head= cur.next
        cur.next = None
        tail.next = head
        
        return new_head
        
        
        
        
            