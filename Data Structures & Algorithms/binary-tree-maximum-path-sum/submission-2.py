# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = -1000

        #post Order DFS
        def dfs(root):
            nonlocal maxSum
            if not root:
                return 0
            
            
            left = max(dfs(root.left),0)
            right = max(dfs(root.right),0)
            maxSum = max(root.val+left+right,maxSum)
            
            return root.val + max(left,right)
        
        dfs(root)
        return maxSum
        