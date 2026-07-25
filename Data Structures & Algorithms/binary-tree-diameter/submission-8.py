# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def diameter(root):

            if not root: return 0,0

            lDiam, lDepth = diameter(root.left)

            rDiam, rDepth = diameter(root.right)
            print(root.val ,max(lDiam, rDiam, 1+rDepth+lDepth), 1+max(rDepth,lDepth))
            return max(lDiam, rDiam, 1+rDepth+lDepth), 1+max(rDepth,lDepth)

        dia, depth = diameter(root)

        return dia-1
        