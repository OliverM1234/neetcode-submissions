# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        out = head = ListNode()
        carry = 0

        while l1 or l2 or carry:
            if not l1:
                n1 = 0
            else:
                n1 = l1.val
                l1 = l1.next
            if not l2:
                n2 = 0
            else:
                n2 = l2.val
                l2 = l2.next

            out.next = ListNode((n1+n2+carry)%10)
            carry = (n1+n2+carry)//10
            out = out.next

        return head.next

        