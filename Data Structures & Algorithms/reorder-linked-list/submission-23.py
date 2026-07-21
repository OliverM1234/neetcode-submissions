# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #find middle of list

        slow = head
        fast = head.next

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        middle = slow


        # reverse second half of the list

        prev = middle
        cur = middle.next
        prev.next = None

        while cur:
            new = cur.next
            cur.next = prev
            prev = cur
            cur = new

        # construct final list

        c1 = head
        c2 = prev


        while c1:
            c1new = c1.next
            c1.next = c2
            c1 = c2
            c2 = c1new


        return None