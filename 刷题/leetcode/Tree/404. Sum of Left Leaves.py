# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
这道题巧妙地方在于
多传一个 bool参数
这个参数 可以帮助判断 是不是left child
因为只有 left child 并且是 leavaf 才可以添加进sums里面去
'''
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sums = 0
        self.helper(root, False)
        return self.sums

    def helper(self, root, left_flag):
        if not root:
            return 0
        if not root.left and not root.right and left_flag:
            self.sums += root.val
            return
        if root.left:
            self.helper(root.left, True)
        if root.right:
            self.helper(root.right, False)