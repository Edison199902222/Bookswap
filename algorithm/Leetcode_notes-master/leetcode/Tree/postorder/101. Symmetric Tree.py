# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        stack = [root.left,root.right]
        while stack:
            l,r = stack.pop(),stack.pop()
            if not l and not r: continue
            if not l or not r : return False
            if l.val != r.val: return False
            stack.append(l.left)
            stack.append(r.right)
            stack.append(l.right)
            stack.append(r.left)
        return True


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.helper(root.left, root.right)

    def helper(self, p, q):
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        left = self.helper(p.left, q.right)
        right = self.helper(p.right, q.left)
        if p.val == q.val and left and right:
            return True
        return False