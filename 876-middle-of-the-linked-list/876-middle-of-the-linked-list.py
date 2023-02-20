class Solution:
    
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        while fast  and fast.next :
            slow = slow.next
            fast = fast.next.next

        return slow
    
#     count = 0
#     cur = head
    
#     while cur:
#         count += 1
#         cur = cur.next
    
#     while count != 0:
#         count -= 1
#         cur = cur.next
    
#     return cur
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     slow = head
#     fast = head

#     while fast and fast.next:
#       slow = slow.next
#       fast = fast.next.next

#     return slow
   




















    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     fast = head

#     while fast and fast.next:
#       slow = slow.next
#       fast = fast.next.next

#     return slow