# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def balanced(root):

            if not root:
                return 0

            lheight = balanced(root.left)
            if lheight == -1:
                return -1

            rheight = balanced(root.right)
            if rheight == -1:
                return -1
            
            if abs(rheight - lheight) > 1:
                return -1

            return 1 + max(lheight, rheight)

        return balanced(root) != -1