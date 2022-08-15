"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

'''
递归方式 解决 没啥说的
'''
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.res = []
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return
        self.res.append(root.val)
        for node in root.children:
            self.helper(node)

'''
这是用非递归 迭代方式解
借用了stack的思想 并且我们从后往前添加元素 进 stack之中 然后每次pop 最后一个元素
这就达到了stack
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        stack = [root]
        res = []
        while stack:
            cur_node = stack.pop()
            if cur_node:
                res.append(cur_node.val)
                if not cur_node.children:
                    continue
                for i in range(len(cur_node.children) - 1, -1, -1):
                    stack.append(cur_node.children[i])
        return res





