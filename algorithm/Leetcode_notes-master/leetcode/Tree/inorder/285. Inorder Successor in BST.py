# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
用中序思想
第一步， 先处理右边子树情况 目的是为了prev指向父节点。 所以先递归右边，然后处理右边，来更新prev
第二步 检查当前层
第三步 更新prev
第四步 处理左边
'''
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        self.result = None
        # prev 指向父节点
        self.prev = None
        self.helper(root, p)
        return self.result

    def helper(self, root, p):
        if root is None or self.result:
            return
            # 递归到最右边,先检查右边的情况
        self.helper(root.right, p)
        # 检查当前层
        if root == p:
            self.result = self.prev
            return
            # 更新prev
        self.prev = root
        # 检查左边
        self.helper(root.left, p)
'''
非递归写法
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        stack = []
        node = root
        # 指向孩子
        prev = None
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if prev is not None and prev == p:
                return node
            prev = node
            node = node.right
        return None


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        self.prev = None
        self.result = None
        self.helper(root, p)
        return self.result

    def helper(self, root, p):
        if not root:
            return
        self.helper(root.left, p)
        # 不能直接return！因为prev 会一直等于p，然后result会一直更新
        if self.prev == p:
            self.result = root
            # return
        self.prev = root
        self.helper(root.right, p)
        return