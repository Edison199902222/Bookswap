# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
建立一个quene
把root放进去
每次pop出来 如果不是None 那么添加左右孩子
并且把本节点作为str加进l中
'''

'''
第二部分先把空格分开
'''
from  collections import deque
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ''
        q = [root]
        l = []
        while q:
            n = q.pop(0)
            if n != None:
                q.append(n.left)
                q.append(n.right)
                l.append(str(n.val))
            else:
                l.append('Null')

        return ' '.join(l)

    def deserialize(self, data):
        if data == '': return None
        array = data.split(' ')
        root = TreeNode(int(array[0]))
        q = [root]
        index = 1
        while q:
            n = q.pop(0)
            if array[index] != 'Null':
                n.left = TreeNode(int(array[index]))
                q.append(n.left)
            index += 1
            if array[index] != 'Null':
                n.right = TreeNode(int(array[index]))
                q.append(n.right)
            index += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))