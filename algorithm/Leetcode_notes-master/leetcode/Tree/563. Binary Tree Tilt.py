# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
每次算 左右的差值 去更新 abs
同时 需要return 到上面 left + right + root的总和
'''
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.abs = 0
        self.helper(root)
        return self.abs

    def helper(self, root):
        if not root:
            return 0
        left, right = self.helper(root.left), self.helper(root.right)
        self.abs += abs(left - right)
        return left + right + root.val