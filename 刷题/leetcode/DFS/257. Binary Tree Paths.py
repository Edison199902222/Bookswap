
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.result = []
        self.helper(root, "")
        return self.result

    def helper(self, root, path):
        if not root:
            return
        if root.left is None and root.right is None:
            path += str(root.val)
            self.result.append(path)
            return
        else:
            path = path + str(root.val) + "->"
        self.helper(root.left, path)
        self.helper(root.right, path)

