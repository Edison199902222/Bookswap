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
class Solution(object):
    def inorderTraversal(self, root):
        if root is None:
            return
        res,stack = [],[]
        while root or stack:
            if root: # travel to each node's left child, till reach the left leaf
                stack.append(root)
                root = root.left
            else:
                temp_node = stack.pop() # this node has no left child
                res.append(temp_node.val)  # so let's append the node value
                root = temp_node.right  # visit its right child --> if it has left child ? append left and left.val, otherwise append node.val, then visit right child again... cur = node.right
        return res

