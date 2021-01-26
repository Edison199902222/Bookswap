# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left, right, result = self.helper(root)
        return result

    # 先考虑清楚，采用后序遍历
    def helper(self, root):
        # 每个node 都有三个状态，左方向时最大的node 数量，右方向时最大的node 数量，result 当前最大的数量
        if not root:
            return -1, -1, -1
        # 后序遍历， 得到左边，右边的状态
        left_l, left_r, result1 = self.helper(root.left)
        right_l, right_r, result2 = self.helper(root.right)
        # 对于当前层，采用左方向的话，下层需要加的是 左边node 采用右方向， 右边node 采用 左方向
        # 最后result 跟 左右 加上当前node，还有不取任何方向时的最大值（意思是放弃当前node）
        return left_r + 1, right_l + 1, max(left_r + 1, right_l + 1, result1, result2)


