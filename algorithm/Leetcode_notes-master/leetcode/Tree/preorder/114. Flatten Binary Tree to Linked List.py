

'''
利用先序遍历
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        list = []
        self.helper(root,list)
        cur = root
        for i in range(1,len(list)):
            cur.left = None
            cur.right = list[i]
            cur = cur.right



    def helper(self,root,list):
        if not root:return
        list.append(root)
        self.helper(root.left,list)
        self.helper(root.right,list)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # 先序遍历
        self.prev = None
        self.helper(root)
    def helper(self, root):
        if root is None:
            return
        # 如果前面有node， 那么 把前面node的right 设置为当前root
        if self.prev is not None:
            self.prev.right = root
            self.prev.left = None
        # 防止更新使得right 消失
        right = root.right
        # prev 更新为当前的root
        self.prev = root
        # 左边弄完了， 弄右边的
        self.helper(root.left)
        self.helper(right)