# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



'''
用dfs一遍一遍往里搜
用pre 保存住前缀 
'''
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.hepler(root,0)

    def hepler(self,root,pre):
        if not root: return 0
        if root.left == None and root.right == None:
            return pre*10+root.val
        left = self.hepler(root.left,pre*10+root.val)
        right = self.hepler(root.right, pre * 10 + root.val)
        return left + right


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = []
        self.helper(root, 0)
        return sum(self.result)
    def helper(self, root, temp):
        if root is None:
            return
        if root.left is None and root.right is None:
            temp = temp * 10 + root.val
            self.result.append(temp)
            return
        self.helper(root.left, temp * 10 + root.val)
        self.helper(root.right, temp * 10 + root.val)