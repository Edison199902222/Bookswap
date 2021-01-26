# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 根据深度来判断，每一层递归返回当前深度，以及底层的root
        depth, node = self.helper(root)
        return node

    def helper(self, root):
        if not root:
            return 0, None
        left_depth, node_left = self.helper(root.left)
        right_depth, node_right = self.helper(root.right)
        if left_depth == right_depth:
            return left_depth + 1, root
        if left_depth < right_depth:
            return right_depth + 1, node_right
        if left_depth > right_depth:
            return left_depth + 1, node_left

