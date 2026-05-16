# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        right_view_nodes = []
        
        def dfs(node, level):
            if not node:
                return 

            if level == len(right_view_nodes):
                right_view_nodes.append(node.val) # because we start with right

            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        dfs(node = root, level = 0)
        return right_view_nodes