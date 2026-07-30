# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def auxValidBST(root, lower, upper):

            if not root:
                return True

            if lower < root.val and root.val  < upper:

                return auxValidBST(root.left, lower, root.val) and auxValidBST(root.right, root.val, upper)

            return False

        return auxValidBST(root, -float('inf'), float('inf'))