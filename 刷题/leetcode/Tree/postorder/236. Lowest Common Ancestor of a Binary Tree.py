'''
用递归
先查找左子树存不存在p或者q
然后查找右子树存不存在p或者q
如果左右都没 return root 说明root是公共祖先
如果左边没 说明在右边
如果右边没有 说明在左边
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left is None:
            return right
        elif right is None:
            return left
        else:
            return root