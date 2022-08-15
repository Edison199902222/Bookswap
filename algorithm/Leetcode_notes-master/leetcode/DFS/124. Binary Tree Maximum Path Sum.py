
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
用一个maxnumber 去hold住最大值
leftsum 跟righjtsum 跟0比较是因为 如果是负数 就舍弃
其实就两种情况 要么 root+left+right是 要么root+left或者right
'''
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_number = float('-inf')
        self.dfs(root)
        return self.max_number

    def dfs(self,root):
        if not root:return 0
        leftsum = max(self.dfs(root.left),0)
        rightsum = max(self.dfs(root.right),0)
        self.max_number = max(self.max_number,leftsum+rightsum+root.val)
        return max(leftsum,rightsum) + root.val


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.result = float("-inf")
        self.helper(root)
        return self.result

    def helper(self, root):
        if root is None:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        max_value = max(left + right + root.val, left + root.val, right + root.val, root.val)
        if max_value > self.result:
            self.result = max_value
        return max(left + root.val, right + root.val, root.val)

