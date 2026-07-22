"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        cur = head
        prevNode = dummy = Node(0)

        nodeHash = {}

        while cur:
            newNode = Node(cur.val)
            nodeHash[cur] = newNode
            prevNode.next = newNode
            prevNode = newNode
            cur = cur.next


        cur = head
        newCur = start = dummy.next

        while cur:

            if cur.random == None:
                randNode = None
            else:
                randNode = nodeHash[cur.random]
            newCur.random = randNode
            cur = cur.next
            newCur = newCur.next

        return start

        

        



        