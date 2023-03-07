# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
#         Recurssive Case
#          TC:O(N) SC:O(N)

        newList=ListNode()
        tail=newList
        
        while(list1 and list2):
            
            if(list1.val<list2.val):
                tail.next=list1
                list1=list1.next
                
            else:
                tail.next=list2
                list2=list2.next
                
            tail=tail.next
            
            
            
        tail.next = list1 or list2
        
        return newList.next
        
        
#         Linked List Approach
        # TC:O(N) & SC:O(1)
#             head1 = List1
#             head2 = List2
            
#             dummy = ListNode()
#             cur = dummy
            
#             while head1 and head2:
#                 if head1.val <= head2.val:
#                     cur.next = ListNode(head1.val)
#                     head1 = head1.next
#                 else:
#                     cur.next = ListNode(head2.val)
#                     head2 = head2.next
#                 cur = cur.next
                
#             if head1:
#                 cur.next = head1
#             if head2:
#                 cur.next = head2
                
#             return dummy.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         dummy =ListNode()
#         tail= dummy  
        
#         while List1 and List2:
#             if List1.val < List2.val :
#                 tail.next = List1
#                 List1= List1.next            
#             else:
#                 tail.next = List2
#                 List2= List2.next 
#             tail =tail.next 
        
        
#         if List1:
#             tail.next = List1
#         elif List2:
#             tail.next = List2
                
#         return dummy.next
    
    #Time complexity: O(n)
    #Space complexity: O1)
        