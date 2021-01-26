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
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif p is None:
            return False
        elif q is None:
            return False
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        if p.val != q.val:
            return False
        return left and right

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:#(dfs)
        stack = [p,q]
        while stack:
            s = stack.pop()
            t = stack.pop()
            if not s and not t:
                continue
            if not s or not t:
                return False
            if s.val != t.val:
                return False
            stack.append(s.left)
            stack.append(t.left)
            stack.append(s.right)
            stack.append(t.right)
        return True