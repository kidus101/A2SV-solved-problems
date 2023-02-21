class Solution:
     def deleteDuplicates(self, head: ListNode) -> ListNode:
            curr = head
            
            while curr and curr.next:
                
                if curr.val == curr.next.val:
                    curr.next = curr.next.next
                else:
                    curr = curr.next
                
            return head
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     curr = head

#     while curr:
#       while curr.next and curr.val == curr.next.val:
#         curr.next = curr.next.next
#       curr = curr.next

#     return head
