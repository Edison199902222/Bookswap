# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        bst, size, min_val, max_val = self.helper(root)
        return size

    def helper(self, root):
        if root is None:
            return True, 0, float("inf"), float("-inf")
        # 返回， 是不是bst， bst的 size， 子树最小值， 最大值 先处理子树
        # 如果不是bst， size 不会更新， 是0
        left_bst, left_size, left_min, left_max = self.helper(root.left)
        right_bst, right_size, right_min, right_max = self.helper(root.right)
        # 判断加上当前层，是不是bst
        # 是的话， 左右size 加上 root的size 就是新的size， 并且flag 设置为true
        if left_bst and right_bst and root.val > left_max and root.val < right_min:
            flag = True
            size = left_size + right_size + 1
        else:
            # 不是的话 flag设置为false， 并且size 是左右子树bst size的最大值
            flag = False
            size = max(left_size, right_size)
        return flag, size, min(left_min, right_min, root.val), max(left_max, right_max, root.val)
