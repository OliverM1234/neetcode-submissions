# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return None
        cur = head
        length = 0

        while cur:
            length += 1
            cur = cur.next

        index = length - n

        prev = realHead = ListNode()
        prev.next = head
        cur = head


        while cur:

            print(index, cur.val)

            if index == 0:
                prev.next = cur.next
                break
            else:
                index -= 1
                prev = cur
                cur = cur.next
        
        return realHead.next



        
        