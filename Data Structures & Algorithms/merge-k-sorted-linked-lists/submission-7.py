class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            merged_lists = []

            for i in range(0,len(lists),2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                merged_lists.append( self.mergeList(list1, list2) )

            lists = merged_lists

        return merged_lists[0]
        
    def mergeList(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        current = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
            
        current.next = l1 or l2
        
        return dummy.next