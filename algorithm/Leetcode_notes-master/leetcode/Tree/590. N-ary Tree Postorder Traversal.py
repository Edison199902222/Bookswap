"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
'''
每次只添加孩子节点
但是 会导致 root没有添加上 所以最后要添加root的val
'''
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        self.res = []
        self.helper(root)
        self.res.append(root.val)
        return self.res

    def helper(self,root):
        if not root:
            return []
        for node in root.children:
            self.helper(node)
            self.res.append(node.val)


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
'''
这个方法更好
每次递归 先把孩子的值 添加到 一个list中
然后再加上自己的值 return
'''

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        if not root.children:
            return [root.val]
        children = []
        for node in root.children:
            children += self.postorder(node)
        return children + [root.val]

