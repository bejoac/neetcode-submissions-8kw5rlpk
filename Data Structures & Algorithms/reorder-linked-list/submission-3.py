# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    
        p, c = None, slow.next
        slow.next = None
        
        while c:
            tmp = c.next
            c.next = p
            p = c
            c = tmp
            
        L, R = head, p

        while R:
            tmpL = L.next
            L.next = R
            tmpR = R.next
            R.next = tmpL
            R = tmpR
            L = tmpL