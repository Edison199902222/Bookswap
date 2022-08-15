# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
先创造一个list 第一个元素代表偷这一层 第二个元素代表不偷
用递归得到左右节点的 偷和不偷的 list
然后更新 偷这一层的话 那么下一层就不能偷result[0] = left[1] + right[1] + root.val
如果不偷这一层 代表下一层可以偷也可以不偷   result[1] = max(left[0], left[1]) + max(right[0], right[1]
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        rob, not_rob = self.dfs(root)
        return max(rob, not_rob)

    def dfs(self, root):
        if root is None:
            return 0, 0
        # 表示 左右子树的情况
        left_rob, left_not_rob = self.dfs(root.left)
        right_rob, right_not_rob = self.dfs(root.right)
        # 当前层的情况 需要依靠 子树的情况
        # 决定偷当前层
        current_rob = left_not_rob + right_not_rob + root.val
        # 决定不偷当前层
        current_not_rob = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
        return current_rob, current_not_rob

