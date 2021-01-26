# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
做法其实差不多

'''


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.helper(root, [], sum)
        return self.result

    def helper(self, root, path, sum):
        if root is None:
            return

        if root.left is None and root.right is None:
            if root.val == sum:
                path.append(root.val)
                self.result.append(path)
            else:
                return

        self.helper(root.left, path + [root.val], sum - root.val)
        self.helper(root.right, path + [root.val], sum - root.val)




