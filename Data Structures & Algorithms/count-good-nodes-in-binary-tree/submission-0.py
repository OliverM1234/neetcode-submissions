# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if root == None:
            return None

        queue = deque()

        queue.append((root,root.val))

        goodNodes = 1

        while queue:

            cur, x = queue.popleft()

            if cur.left:
                if cur.left.val >= x:
                    goodNodes += 1
                    out_val = cur.left.val
                else:
                    out_val = x
                queue.append((cur.left,out_val))
            if cur.right:
                if cur.right.val >= x:
                    goodNodes += 1
                    out_val = cur.right.val
                else:
                    out_val = x
                queue.append((cur.right,out_val))

        return goodNodes




            