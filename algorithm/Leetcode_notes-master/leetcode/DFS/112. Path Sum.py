# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
dfs 一个一个走
'''


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.helper(root, sum)

    def helper(self, root, sum):
        if root is None:
            return False
        if root.left is None and root.right is None:
            if root.val == sum:
                return True
            else:
                return False
        return self.helper(root.left, sum - root.val) or self.helper(root.right, sum - root.val)
if __name__=='__main__':
    solution=Solution()
    A1 = TreeNode(5)
    A2 = TreeNode(4)
    A3 = TreeNode(8)
    A4 = TreeNode(2)
    A5 = TreeNode(1)

    A1.left=A2
    A1.right=A3
    A2.left=A4
    A2.right=A5
    print(solution.hasPathSum(A1,11))
