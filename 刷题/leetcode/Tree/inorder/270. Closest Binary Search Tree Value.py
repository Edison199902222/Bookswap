
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.result = float("inf")
        self.helper(root, target)
        return self.result

    def helper(self, root, target):
        if not root:
            return
        self.helper(root.left, target)
        if abs(root.val - target) == 0:
            self.min = root.val
            return
        if abs(root.val - target) < abs(self.result - target):
            self.result = root.val
        self.helper(root.right, target)
        return

