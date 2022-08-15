# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        self.helper(root)
        return self.result

    def helper(self, root):
        if root is None:
            return 0, 0
        # 当前升序列 降序咧
        increase_length = 1
        decrease_length = 1
        # 得到 以root为端点时 左边 最长升序， 跟 降序
        left_increase, left_decrease = self.helper(root.left)
        # 得到 得到 以root为端点时 右边 最长升序， 跟 降序
        right_increase, right_decrease = self.helper(root.right)
        # 更新 当前 最长升序列， 跟降序
        if root.left:
            if root.left.val + 1 == root.val:
                increase_length = max(increase_length, left_increase + 1)
            if root.left.val - 1 == root.val:
                decrease_length = max(decrease_length, left_decrease + 1)
        if root.right:
            if root.right.val + 1 == root.val:
                increase_length = max(increase_length, right_increase + 1)
            if root.right.val - 1 == root.val:
                decrease_length = max(decrease_length, right_decrease + 1)
        # 最长的组成肯定是， 一边升序 一边降序， 这样组合起来就是最长的
        self.result = max(self.result, increase_length + decrease_length - 1)
        # 返回以当前root 为端点时， 最长升序， 跟降序
        return increase_length, decrease_length


