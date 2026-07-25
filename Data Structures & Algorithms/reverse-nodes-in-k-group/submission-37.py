# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        i=1
        curList = start = head
        out = outStart = ListNode()

        while curList:

            if i < k:
                i += 1
                curList = curList.next
            else:
                i = 1
                end = curList
                curList = curList.next
                end.next = None

                prev = start
                cur = start.next
                prev.next = None

                while cur:
                    new = cur.next
                    cur.next = prev
                    prev = cur
                    cur = new

                out.next = end
                out = start
                start = curList
        out.next = start
        return outStart.next