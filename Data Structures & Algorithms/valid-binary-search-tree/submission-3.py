# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #Pre Order DFS:

        def dfs(root,leftlimit,rightlimit):
            if not root:
                return True
            
            if root.val<=leftlimit or root.val>=rightlimit:
                return False
            
            return dfs(root.left,leftlimit,root.val) and dfs(root.right,root.val,rightlimit)
        
        return dfs(root,-1001,1001)
            
        