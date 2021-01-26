# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.helper(root, None)
        return self.ans

    def helper(self, root, parent):
        if not root:
            return True
        left = self.helper(root.left, root.val)
        right = self.helper(root.right, root.val)
        if left and right:
            self.ans += 1
        return left and right and root.val == parent
'''
这是 botom to up
首先 我们递归到 叶子节点
对于叶子节点来说 左右没有孩子 肯定是一个uni value
对于每一次递归 我们递归到下一层时， 记录父亲节点的值
这样 我们 每一次只需要判断 left 跟right 是不是true 就行了
意思是 left 跟 right 除了检查左边子树 跟右边子树 自己是不是univalue 还检查了 左子树 跟 右子树 跟 自己的值是不是相等
如果 三个都相等，说明自己也是一个univale
所以 每一次需要return left 跟 right 还需要判断 自己的值 跟父亲节点的值一不一样
'''