# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder):
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]

        for i in range(1, len(preorder)):
            node = TreeNode(preorder[i])

            if node.val < stack[-1].val:
                stack[-1].left = node
                stack.append(node)
                
            else:
                while stack and node.val > stack[-1].val:
                    last = stack.pop()

                last.right = node
                stack.append(node)

        return root

        