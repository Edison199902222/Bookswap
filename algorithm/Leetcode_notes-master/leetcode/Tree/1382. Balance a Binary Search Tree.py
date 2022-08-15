# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.order = []
        self.inorder(root)
        start = 0
        end = len(self.order) - 1
        mid = (start + end) // 2
        root = TreeNode(self.order[mid])
        root.left = self.builder(start, mid - 1)
        root.right = self.builder(mid + 1, end)
        return root

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.order.append(root.val)
        self.inorder(root.right)

    def builder(self, start, end):
        if start > end:
            return
        mid = (start + end) // 2
        node = TreeNode(self.order[mid])
        node.left = self.builder(start, mid - 1)
        node.right = self.builder(mid + 1, end)
        return node

'''
变成balance bst 
首先把bst 用inorder 添加进list 
然后用builder 函数 构建balance bst 每次 把mid 当成node 左子树就是左半边list 右子树就是右边list
'''