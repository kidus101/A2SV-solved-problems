# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        queue = deque()
        queue.append(root)
        answer = []
        
        while queue:
            level_length = len(queue)
            total = 0
            
            for _ in range(level_length):
                cur = queue.popleft()
                total += cur.val
                
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            
            answer.append(total / level_length)
            
        return answer
        