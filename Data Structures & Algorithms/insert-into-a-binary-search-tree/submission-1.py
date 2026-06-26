# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val=val)

        stack = [root]

        while stack:
            node = stack.pop()

            if val < node.val:
                if node.left:
                    stack.append(node.left)
                else:
                    node.left = TreeNode(val=val)

            elif val > node.val:
                if node.right:
                    stack.append(node.right)
                else:
                    node.right = TreeNode(val=val)

        return root
