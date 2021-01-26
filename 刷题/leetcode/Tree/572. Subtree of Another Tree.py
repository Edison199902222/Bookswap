# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
对比两个tree 是不是一样（t 有可能是 s的 subtree）
那么我们就可以先check 他们的root 是不是相等
如果相等 那么我们就用 is_same 这个函数 去检查 下面的node是不是相等的
如果不相等 那么我们就递归到s的左边孩子 跟右边孩子 继续 check
'''
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val == t.val and self.is_same(s, t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def is_same(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        return self.is_same(s.left, t.left) and self.is_same(s.right, t.right)