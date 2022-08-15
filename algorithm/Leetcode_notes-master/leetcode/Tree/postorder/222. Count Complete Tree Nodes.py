# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
完全二叉树意思是 除了最后一层叶子节点 有可能不是满的外 其他层 全是满 并且 最后一层的node是从左往右排列的
满二叉树意思是 全是满的node 2^d - 1
我们先用分治法 得到 左边子树的长度 和右边子树的长度
因为这是一个完全二叉树 所以
如果左右长度相等 那么左边肯定是一个满二叉树 因为 在同一层而言 右边有node的前提下 是左边插满了node
如果左边比右边长度多 那么右边肯定是一个满的二叉树 因为只有右边满了的情况下 才能有继续拓展左边

'''
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        if left == right:
            return 2 ** left + self.countNodes(root.right)
        else:
            return 2 ** right + self.countNodes(root.left)

    def helper(self, root):
        if not root:
            return 0
        return self.helper(root.left) + 1