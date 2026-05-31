# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        candidates = []

        def dfs(node):
            if not node:
                return 

            dfs(node.left)
            
            if len(candidates) < k:
                candidates.append(node.val)
            else:
                return 

            dfs(node.right)

        dfs(root)
        return candidates[-1]