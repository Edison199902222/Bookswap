# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
每次把一条路径的最小值找出来
low 跟 high 始终存储的是 这条路径上 最接近的数
每次递归左边的时候 我们要把 root 作为 high 因为这时候low会更接近high
递归右边的时候  要把root 作为low 因为这时候 low会更接近high
'''
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        high = float('inf')
        low = float('-inf')
        return self.helper(root, low, high)

    def helper(self, root, low, high):
        if not root:
            return high - low
        left = self.helper(root.left, low, root.val)
        right = self.helper(root.right, root.val, high)
        return min(left, right)
