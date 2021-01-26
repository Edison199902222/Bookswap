# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
用stack 一个用来存储每一层的node
一个用来储存最终结果

'''
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return None
        result = [root]
        final_result = []
        while len(result) != 0:
            node = result.pop()
            final_result.append(node.val)
            if node.right:
                result.append(node.right)
            if node.left:
                result.append(node.left)
        return final_result
'''
The 2nd uses modified preorder (right subtree first). Then reverse the result.'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result