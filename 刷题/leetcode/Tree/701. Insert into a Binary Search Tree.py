# 利用bst 的特征
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        return self.helper(root, val)

    def helper(self, root, val):
        # 如果没有node，代表要加一个node了
        if not root:
            return TreeNode(val)
        if root.val < val:
            root.right = self.helper(root.right, val)
        else:
            root.left = self.helper(root.left, val)
        return root



class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        return self.helper(root, val)

    def helper(self, root, val):
        if not root:
            return None
        if root.val < val:
            temp = self.helper(root.right, val)
            if temp is None:
                root.right = TreeNode(val)
        else:
            temp = self.helper(root.left, val)
            if temp is None:
                root.left = TreeNode(val)
        return root