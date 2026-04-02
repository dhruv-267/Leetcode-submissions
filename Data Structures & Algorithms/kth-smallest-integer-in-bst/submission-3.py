# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        while root:
            if not root.left:
                k-=1
                if k == 0:
                    return root.val
                root = root.right
            else:
                pred = root.left
                while pred.right and pred.right!= root:
                    pred= pred.right
                if not pred.right:
                    pred.right = root
                    root = root.left
                else:
                    pred.right = None
                    k-=1
                    if k == 0:
                        return root.val
                    root = root.right
        return -1
        