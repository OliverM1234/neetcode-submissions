# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = deque()
        out = []
        if not root:
            return []

        queue.append(root)
        i=0

        while queue:

            n = len(queue)

            out.append(queue[n-1].val)

            for i in range(n):

                cur = queue.popleft()

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)


        return out