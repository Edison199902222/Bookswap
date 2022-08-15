# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
先用一个 global variable res
res 作用是 保存最大直径
然后每次对于每一个node  也就是每一次递归
我们都先找到他左孩子能提供最大的直径 跟右孩子能提供的最大直径
然后 l+r 去跟 之前的res比较 如果比res 大 那么就更新 因为 无论什么情况 l + r 加起来提供的路径永远是最多的
然后 我们取 左孩子 跟 右孩子的最大值 并且加上当前root到上一层的长度 返回到上一层去
'''
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.helper(root)
        return self.res

    def helper(self, root):
        if root is None:
            return 0
        l = self.helper(root.left)
        r = self.helper(root.right)
        self.res = max(self.res, l + r)
        return max(l, r) + 1