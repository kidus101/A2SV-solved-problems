# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> Optional[TreeNode]:
        if tree1 and tree2:
                
                root = TreeNode(tree1.val + tree2.val)
                root.left = self.mergeTrees(tree1.left, tree2.left)
                root.right = self.mergeTrees(tree1.right, tree2.right)
                
                return root
        
        else:
            return tree1 or tree2