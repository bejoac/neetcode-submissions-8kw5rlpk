# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution: 
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_deque, q_deque = deque([p]),  deque([q])

        while p_deque and q_deque:
            p_node = p_deque.popleft()
            q_node = q_deque.popleft()

            if not p_node and not q_node:
                continue
            elif not p_node and q_node:
                return False
            elif p_node and not q_node:
                return False

            if p_node.val != q_node.val:
                return False


            p_deque.append(p_node.left)
            p_deque.append(p_node.right)

            q_deque.append(q_node.left)
            q_deque.append(q_node.right)

        return True
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        root_deque = deque([root])

        while root_deque:
            node = root_deque.popleft()
            if not node:
                continue
                
            if node.val == subRoot.val:
                if self.isSameTree(node, subRoot):
                    return True

            root_deque.append(node.left)
            root_deque.append(node.right)

        return False