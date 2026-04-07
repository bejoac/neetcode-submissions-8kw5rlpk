# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        L = head
        R = head.next

        while R and R.next:        
            if L == R:
                return True
            
            if L == None or R == None:
                return False

            L = L.next
            R = R.next.next

        return False