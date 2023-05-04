# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def preorder(node):
            nonlocal index, res
            if not node:
                return 
            preorder(node.left)
            index+=1
            if index == k: 
                res = node.val
            preorder(node.right)
        res = 0
        index = 0
        preorder(root)
        return res
            
