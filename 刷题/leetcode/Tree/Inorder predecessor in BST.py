# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        # 每次指向孩子
        self.child = None
        self.result = None
        self.helper(root, p)
        return self.result

    def helper(self, root, p):
        if not root or self.result:
            return
        self.helper(root.left, p)
        if root == p:
            self.result = self.child
        self.child = root
        self.helper(root.right, p)
        return