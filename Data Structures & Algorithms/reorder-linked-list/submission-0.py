# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        
        def walk(node):
            if not node:
                return 
            
            nodes.append(node)
            walk(node.next)
        
        walk(head)
        
        L, R = 0, len(nodes) - 1
        
        while L < R:
            nodes[L].next = nodes[R]
            L = L + 1
            nodes[R].next = nodes[L]
            R = R - 1

        nodes[L].next = None