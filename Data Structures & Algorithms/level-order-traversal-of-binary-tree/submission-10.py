# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque()
        out = []
        level = 0

        queue.append(root)

        while queue:

            l = len(queue)
            cur_out = []

            for i in range(l):
                cur = queue.popleft()

                if cur:
                    cur_out.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)

            if cur_out:
                out.append(cur_out)


        return out

        
        