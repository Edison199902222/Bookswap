# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        while root:
            temp = []
            if self.dfs(root, temp):
                root = None
            result.append(temp)
        return result

    def dfs(self, root, temp):
        if not root:
            return False
        if not root.left and not root.right:
            temp.append(root.val)
            return True
        if self.dfs(root.left, temp):
            root.left = None
        if self.dfs(root.right, temp):
            root.right = None
        return
