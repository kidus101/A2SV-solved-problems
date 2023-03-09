# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def findMode(self, root: TreeNode) -> List[int]:
        
        list_ = []                           
        dic = {}                            
        max_ = 0                            
        
        def find(root):
            
            if not root:                   
                return
            
            if root.val in dic:             
                dic[root.val] += 1
                
            else:
                dic[root.val] = 1           
            
            find(root.left)
            find(root.right)
            
            return 
     
        find(root)
        
        dicval_list = list(dic.values())   
        max_ = max(dicval_list)             
        
        for key, value in dic.items():
            if value == max_:               
                list_.append(key)
                
        return list_