# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        answer = []
       
        if not root:
            return []
        
        while queue:
            level_length = len(queue)
            total = []
            
            for i in range(level_length):
                cur = queue.popleft()
                if cur:
                    total.append(cur.val)
                
                if cur and cur.left:
                    queue.append(cur.left)
                if cur and cur.right:
                    queue.append(cur.right)
            
            answer.append(total )
            
        return answer
         
            
            
            
            
            
            
            
            
            
            
            
        
#         self.res = []       
        
#         def traverse(root, level = 0):
            
#             if not root: return    
            
#             if len(self.res) <= level:      
#                 self.res.append([root.val])
                
#             else:
#                 self.res[level].append(root.val)    #
            
#             traverse(root.left, level + 1)      #
#             traverse(root.right, level + 1)
            
#         traverse(root)
        
#         return self.res # return results
        