# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            outList = list1
            list1 = list1.next
        else:
            outList = list2
            list2 = list2.next

        head = outList
        
        while list1 or list2:

            if not list1:
                outList.next = list2
                list2 = list2.next
            elif not list2:
                outList.next = list1
                list1 = list1.next
            elif list1.val < list2.val:
                outList.next = list1
                list1 = list1.next
            else:
                outList.next = list2
                list2 = list2.next

            outList = outList.next

        return head


        