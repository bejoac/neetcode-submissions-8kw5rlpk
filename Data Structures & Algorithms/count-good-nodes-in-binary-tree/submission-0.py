# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        count_good = 0

        def dfs(node, largest_path_value):
            nonlocal count_good
            
            if not node:
                return 

            if node.val >= largest_path_value:
                count_good += 1
                largest_path_value = node.val

            dfs(node.left, largest_path_value)
            dfs(node.right, largest_path_value)

        dfs(root, -101)
        return count_good
            
