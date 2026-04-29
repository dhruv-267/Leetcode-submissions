# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = True
        def dfs(p,q):
            nonlocal res
            if not p and not q:
                return
            elif not p or not q or p.val!= q.val:
                res = False
                return

            dfs(p.left,q.left)
            dfs(p.right,q.right)
            return
        dfs(p,q)
        return res

            
            
            


        """
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        """