# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidSequence(self, root, arr):
        """
        :type root: TreeNode
        :type arr: List[int]
        :rtype: bool
        """
        return self.helper(root, arr, 0)

    def helper(self, root, arr, index):
        if not root or index >= len(arr) or root.val != arr[index]:
            return False
        if (not root.left) and (not root.right) and index == len(arr) - 1:
            return True
        return self.helper(root.left, arr, index + 1) or self.helper(root.right, arr, index + 1)
