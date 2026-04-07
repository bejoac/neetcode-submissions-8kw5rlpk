# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        
        if list1.val <= list2.val:
            root = list1
            if list1.next:
                p1 = list1.next
                p2 = list2
            else:
                root.next = list2
                return root

        elif list1.val > list2.val:
            root = list2
            if list2.next:
                p1 = list1
                p2 = list2.next
            else:
                root.next = list1
                return root

        cur = root

        while p1 or p2:
            if p1.val <= p2.val:
                cur.next = p1
                cur = p1
                p1 = p1.next
            elif p1.val > p2.val:
                cur.next = p2
                cur = p2
                p2 = p2.next

            if not p1:
                cur.next = p2
                p2 = None
            elif not p2:
                cur.next = p1
                p1 = None


        return root