# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        return self.helper(root, set(), k)

    def helper(self, root, root_set, k):
        if not root:
            return False
        temp = k - root.val
        if temp in root_set:
            return True
        root_set.add(root.val)
        return self.helper(root.left, root_set, k) or self.helper(root.right, root_set, k)
'''
用一个set 去保存 每一个node
然后在每一层 我们需要检查 target - 这一层的值 是不是在之前的node set中存在 如果存在 直接return true
如果不存在 那么继续递归 左孩子 跟右孩子
'''