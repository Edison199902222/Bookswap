# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        # 一个subtree， 每次需要返回的是整个树的 node 和 sum，不能像选path 一样选择 其中之一
        self.result = float("-inf")
        self.helper(root)
        return self.result

    def helper(self, root):
        if not root:
            return 0, 0
        left_sum, left_number = self.helper(root.left)
        right_sum, right_number = self.helper(root.right)
        cur_sum, cur_number = left_sum + right_sum + root.val, left_number + right_number + 1
        self.result = max(self.result, cur_sum / cur_number)
        return cur_sum, cur_number