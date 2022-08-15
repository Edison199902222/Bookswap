"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

"""
这道题 用dfs递归做
首先 如果root 左边不为空 说明root左右都有孩子
只需要 root的左孩子的next指向右边孩子就行
还需要 判断 如果root的next不为none的话 说明这个root不是根结点 并且不是叶子结点
还需要把 root的右孩子的next 指向root next的左孩子
  0 -> null
   /     \
  2  ->   4 -> null
 / \     / \
6-> 8->10-> 12 -> nul
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None or root.left == None: return  root
        root.left.next = root.right
        if root.next!=None:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node.left and node.right:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                queue.append(node.left)
                queue.append(node.right)
        return root

