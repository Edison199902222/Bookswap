# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.result = True
        self.helper(root)
        return self.result

    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        if abs(left - right) >= 2:
            self.result = False
        return 1 + max(left, right)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        height, result = self.helper(root)
        return result

    def helper(self, root):
        if root is None:
            return 0, True
        left_height, flag1 = self.helper(root.left)
        right_height, flag2 = self.helper(root.right)
        if not flag1 or not flag2:
            return 1 + max(left_height, right_height), False
        if abs(left_height - right_height) >= 2:
            return 1 + max(left_height, right_height), False
        else:
            return 1 + max(left_height, right_height), True

