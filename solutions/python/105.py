# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def construct(left, right):
            nonlocal rootindex
            if left > right:
                return None

            rootvalue = preorder[rootindex]
            rootindex+=1
            node = TreeNode(rootvalue)

            inorderindex=0
            for i,num in enumerate(inorder):
                if num == rootvalue:
                    inorderindex=i
            node.left=construct(left, inorderindex-1)
            node.right=construct(inorderindex+1, right)

            return node
        rootindex=0
        return construct(0,len(inorder)-1)