
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)

    def helper(self, root):
        if root is None:
            return 0
        if not root.left:
            return 1 + self.helper(root.right)
        if not root.right:
            return 1 + self.helper(root.left)
        left_depth = self.helper(root.left)
        right_depth = self.helper(root.right)
        return 1 + min(left_depth, right_depth)