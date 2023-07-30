# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        height_diff = 0
        def dfs(root):
            nonlocal height_diff
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            height_diff = max(height_diff, abs(left - right))
            return 1 + max(left, right)
        dfs(root)
        return True if height_diff < 2 else False
