# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def isLeaf(node):
            if not node.left and not node.right:
                return True
            return False
        def dfs(node, path):
            if not node:
                return
            path.append(node.val)
            if isLeaf(node) and sum(path)==targetSum:
                res.append(path[:])
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            path.pop()
    
        res = []
        dfs(root, [])
        return res