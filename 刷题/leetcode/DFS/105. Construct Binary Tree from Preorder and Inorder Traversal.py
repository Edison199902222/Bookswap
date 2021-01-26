# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
前序加中序
前序第一个结点可以知道root是什么
然后定位root在inorder之中 左边就是left 右边就是right
'''

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(inorder) == 0:return None
        rootindex = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:rootindex+1],inorder[:rootindex])
        root.right = self.buildTree(preorder[rootindex+1:],inorder[rootindex+1:])
        return root