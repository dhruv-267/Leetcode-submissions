# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = [0]

        def dfs(root):
            if not root:
                return -1
            
            left = dfs(root.left)
            right = dfs(root.right)

            res[0] = max(res[0], 2+left+right)

            return 1 + max(left,right)
        
        
        dfs(root)
        return res[0]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        #dfs
        res = [0]

        #post order dsf
        def dfs(root):
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
        '''