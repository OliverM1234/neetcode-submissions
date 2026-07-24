# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        dummy = start = ListNode()

        for i in range(len(lists)):

            list1 = start.next
            list2 = lists[i]
            dummy = start

            while list1 and list2:

                if list1.val < list2.val:

                    dummy.next = list1
                    list1 = list1.next

                else:

                    dummy.next = list2
                    list2 = list2.next

                dummy = dummy.next

            dummy.next = list1 or list2

        return start.next        