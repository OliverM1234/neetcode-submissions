# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        cnt = 0
        res = None

        def inOrder(root):
            nonlocal cnt, res

            if not root or res is not None:
                return

            inOrder(root.left)

            cnt+=1
            if cnt == k:
                res = root.val
            
            inOrder(root.right)

        inOrder(root)

        return res