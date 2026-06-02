"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {}

        dummy = Node(0)
        orig_cur = head
        copy_prev = dummy

        while orig_cur:
            if orig_cur in node_map:
                copy_cur = node_map[orig_cur]
            else:
                copy_cur = Node(orig_cur.val)
                
            copy_prev.next = copy_cur # Link
            
            node_map[orig_cur] = copy_cur
            
            if orig_cur.random:
                    if orig_cur.random not in node_map:
                        random_copy = Node(x=orig_cur.random.val)
                        node_map[orig_cur.random] = Node(x=orig_cur.random.val)
                    copy_cur.random = node_map[orig_cur.random]
                    

            copy_prev = copy_cur
            orig_cur = orig_cur.next

        return dummy.next