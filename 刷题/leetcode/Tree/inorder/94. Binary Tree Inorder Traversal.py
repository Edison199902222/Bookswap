# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Recursion one
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.helper(root,res)
        return res

    def helper(self,root, res):
        if root is None:
            return
        if root.left:
            self.helper(root.left,res)
        res.append(root.val)
        if root.right:
            self.helper(root.right,res)
#  iterative
'''
这道题用迭代的方法比递归复杂
先往stack里面加入左node
直到没有左node
然后再pop出最左边的leaf（无左孩子）
把它加进res
如果这个node 有右边孩子
那么继续加进stack里面 
'''
c# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        # stack 列表 最后面 储存的即将要print的节点
        stack = []
        node = root
        while node or stack:
            while node:
                # 储存从所有 父节点 到 所有左边的节点
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.val)
            # 如果当前最左的节点 有 右子树的话，我们要先print 右边的树
            # 因为是inorde， 我们当前最左node 已经print了，就需要检查print 右边的子树， 左 -> 根 -> 右
            node = node.right
        return result

