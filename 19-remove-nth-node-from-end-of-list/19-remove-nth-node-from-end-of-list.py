class Solution:
    def removeNthFromEnd(self, head: ListNode, k: int) -> ListNode:
        
        
        
        dummy = ListNode(0 , head)
        
        temp = head
        length = 0
        
        while temp:
            temp = temp.next
            length += 1
        
        if length == 1:
            return head.next
        
        prev = dummy
        cur = head
        
        for i in range(length - k):
            prev = cur 
            cur = cur.next
        
        prev.next = cur.next
        
        return dummy.next     
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     slow = head
#     fast = head

#     for _ in range(n):
#       fast = fast.next
#     if not fast:
#       return head.next

#     while fast.next:
#       slow = slow.next
#       fast = fast.next
#     slow.next = slow.next.next

#     return head
