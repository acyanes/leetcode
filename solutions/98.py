# ======= Recursive solution ==========
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, maxval, minval):
            if not node:
                return True
            
            if node.val <= minval or node.val >= maxval:
                return False
            
            return dfs(node.left, node.val, minval) and dfs(node.right, maxval, node.val)

        return dfs(root, math.inf, -math.inf)

          

# ======= Iterative solution ==========
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        stack=[(root, -math.inf, math.inf)]
        while stack:
            curr,low,high = stack.pop()
            if curr.val <= low or curr.val >= high:
                return False
            if curr.left:
                stack.append((curr.left, low, curr.val))
            if curr.right:
                stack.append((curr.right, curr.val, high)) 
        return True
