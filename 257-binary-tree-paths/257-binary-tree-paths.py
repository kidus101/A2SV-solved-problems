# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_path(self, root: Optional[TreeNode], cur, res) -> None:
        
        if not root:
            return
        
        cur.append(str(root.val))
        
        if not root.left and not root.right:
            res.append('->'.join(cur))
            
        self.find_path(root.left, cur, res)
        self.find_path(root.right, cur, res)
        
        cur.pop()
        
        
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        self.find_path(root, [], res)
        return res