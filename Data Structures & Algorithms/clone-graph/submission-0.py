"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtonew = {}

        def clone(node):
            # Base case
            if node in oldtonew:
                return oldtonew[node]

            # Recursive case
            copy = Node(val=node.val)
            oldtonew[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))
            
            return copy

        return clone(node) if node else None