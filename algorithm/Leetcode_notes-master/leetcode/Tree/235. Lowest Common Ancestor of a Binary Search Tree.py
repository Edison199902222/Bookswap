'''
因为是二叉搜索树
所以root比左边的大 比右边的小
就很直观了
如果root比 p 和 q都大 说明p q存在左边
如果比 p q都小 说明存在右边
不然就一左一右 返回root就行了
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if  p.val< root.val > q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if q.val > root.val < p.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root