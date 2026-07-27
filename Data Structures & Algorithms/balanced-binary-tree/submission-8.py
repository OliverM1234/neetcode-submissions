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
                return True, 0

            lbalanced, lheight = balanced(root.left)
            rbalanced, rheight = balanced(root.right)
            dif = lheight - rheight

            return lbalanced and rbalanced and (-1 <= dif) and (dif <= 1), 1 + max(lheight,rheight)

        return balanced(root)[0]