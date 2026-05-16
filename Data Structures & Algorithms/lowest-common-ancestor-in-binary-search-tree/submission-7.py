# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root, p, q):

        queue = deque([root])

        while queue:
            node = queue.pop()

            if (p.val < node.val and q.val > node.val) or (p.val > node.val and q.val < node.val):
                return node

            if node.val == p.val:
                return node
            if node.val == q.val:
                return node

            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)




