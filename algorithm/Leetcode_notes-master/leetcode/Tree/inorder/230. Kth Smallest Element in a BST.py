# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
先递归到树的最左叶节点
然后k-1 去检查当前最左节点是不是最小第k个
如果不是 则return到父节点
然后父节点检查自己是不是
再检查右边是不是 最小第k个
总结 就是先检查左边 然后检查自己 再检查右边
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.result = None
        self.helper(root)
        return self.result

    def helper(self, root):
        if root is None:
            return
        self.helper(root.left)
        self.k -= 1
        if self.k == 0:
            self.result = root.val
            return
        else:
            self.helper(root.right)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right
        return None
