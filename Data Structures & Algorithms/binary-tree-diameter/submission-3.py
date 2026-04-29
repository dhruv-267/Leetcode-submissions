# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        #dfs
        res = [0]       # res = 0 <-- nonlocal; non mutable variable as it is outside of dfs scope

        #post order dsf
        def dfs(root):
            # nonlocal res     if we want to use outside non mutable variable as local variable
            if not root:
                return -1
            
            left = dfs(root.left)
            right = dfs(root.right)
            #diameter = height of left child + height of right child + 2
            dia = left + right + 2
            res[0] = max(res[0],dia)

            return 1 + max(left,right)
        dfs(root)
        return res[0]