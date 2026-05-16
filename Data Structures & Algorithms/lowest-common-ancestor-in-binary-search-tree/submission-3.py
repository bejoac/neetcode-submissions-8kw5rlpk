# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def search_subtree(self, root: TreeNode, target: TreeNode) -> bool:
        queue = deque([root])
        
        while queue:
            node = queue.pop()
            if node.val == target.val:
                return True
            
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)
                
        return False

    def lowestCommonAncestor(self, root, p, q):

        queue = deque([(root, None)])

        while queue:
            node, parent = queue.pop()
            if (p.val < node.val and q.val > node.val) or (p.val > node.val and q.val < node.val):
                return node

            if node.val == p.val:
                if self.search_subtree(root=node, target=q):
                    return node
                else:
                    return parent if parent else root

            if node.val == q.val:
                if self.search_subtree(root=node, target=p):
                    return node
                else:
                    return parent if parent else root

            if node.left:
                queue.appendleft((node.left, node))
            if node.right:
                queue.appendleft((node.right, node))




