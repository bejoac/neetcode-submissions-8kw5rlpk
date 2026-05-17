# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)
        L = dummy
        R = head
        
        while n > 0:
            R = R.next
            n -= 1
        
        while R:
            L = L.next
            R = R.next
        
        L.next = L.next.next
        return dummy.next