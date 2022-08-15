# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 前序遍历，往右先遍历
        self.prev = 0
        self.helper(root)
        return root

    def helper(self, root):
        if not root:
            return
        self.helper(root.right)
        root.val += self.prev
        self.prev = root.val
        self.helper(root.left)
        return


