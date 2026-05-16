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

        queue = deque([(root, 0)]) # (node, level) 
        nested = []

        while queue:
            node, level = queue.pop()       
            
            if len(nested) == level: # wenn noch keine liste für das level 
                nested.append([node.val])
            else:
                nested[level].append(node.val)
            
            if node.left:
                queue.appendleft((node.left, level + 1))
            if node.right:
                queue.appendleft((node.right, level + 1))

        right_side_view = []
        for level in nested:
            right_side_view.append(level[-1])
        return right_side_view