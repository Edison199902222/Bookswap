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
        self.helper(root, 0, None)
        return self.result

    def helper(self, root, sums, parent):
        if not root:
            return
        if parent != None and root.val == parent + 1:
            sums += 1
        else:
            sums = 1
        self.result = max(self.result, sums)

        left = self.helper(root.left, sums, root.val)
        right = self.helper(root.right, sums, root.val)
'''
每一次递归 我们要做的事
base cause  如果root 是None 我们 return
然后每一次 我们检查 如果parent 不是 None， 并且当前root 等于parent 的值 +1 的话，说明我们可以把之前的sums + 1
如果不是的话， sums需要重新开始 变成1
然后我们更新 最大值
继续递归 左子树 跟右子树
'''