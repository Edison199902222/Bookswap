# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.heler(root,res)
        return res
    def heler(self,root,res):
        if root is None:
            return
        self.heler(root.left,res)
        self.heler(root.right,res)
        res.append(root.val)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = [[root, False]]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    # 说明第二次回到这个节点
                    result.append(node.val)
                else:
                    stack.append([node, True])
                    stack.append([node.right, False])
                    stack.append([node.left, False])
        return result
'''
第一步 确定每个node需要第二次回到节点时再print，stack中每一个元素储存 node 跟 当前访问是否为第二次
第二步 第一次访问节点时，添加自己节点，并且把左右孩子放进stack中
'''