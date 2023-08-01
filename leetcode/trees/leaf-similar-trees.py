# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def traverse(root, arr):
            if root:
                traverse(root.left, arr)
                if not root.left and not root.right:
                    arr.append(root.val)
                traverse(root.right, arr)
        tree1 = []
        tree2 = []
        traverse(root1, tree1)
        traverse(root2, tree2)
        print(tree1, tree2)
        return tree1 == tree2
