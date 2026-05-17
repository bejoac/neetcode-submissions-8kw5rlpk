# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        next_node = head
        
        while next_node:
            length += 1
            next_node = next_node.next
        
        # Head removal
        if n == length:
            tmp = head.next
            head = tmp
            return head
            
        p, c = None, head
        
        for _ in range(length - n):
            p = c
            c = c.next
        
        p.next = c.next
        return head