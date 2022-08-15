'''
使用中序遍历
每次检查，孩子节点是不是小于自己的值
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.child = None
        self.is_BST = True
        self.helper(root)
        return self.is_BST

    def helper(self, root):
        if root is None:
            return
        self.helper(root.left)
        if self.child is not None and self.child >= root.val:
            self.is_BST = False
            return
        self.child = root.val
        self.helper(root.right)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        stack = []
        prev = None
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if prev and node.val <= prev.val:
                return False
            prev, node = node, node.right
        return True




