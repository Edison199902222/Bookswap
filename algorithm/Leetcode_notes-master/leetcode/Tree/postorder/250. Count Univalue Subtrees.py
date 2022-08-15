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
left 跟 right return的 意思是， 左边子树所有的值 跟自己的值 跟 右边子树所有值 都相等
所以 如果left 跟 right 都是true 的话， 说明 自己是一个uni value 所以 + 1
所以 对于每一个node 来说， 我们只需要判断自己是不是
所以 每一次需要return left 跟 right 还需要判断 自己的值 跟父亲节点的值一不一样
'''