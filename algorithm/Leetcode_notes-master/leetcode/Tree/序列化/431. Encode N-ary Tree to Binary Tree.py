"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Codec:
    def encode(self, root):
        """Encodes an n-ary tree to a binary tree.
        :type root: Node
        :rtype: TreeNode
        """
        if not root:
            return None
        # 把下一层的第一个设置为左孩子，然后之后的孩子全部设置为 前面一个的右孩子
        rootNode = TreeNode(root.val)
        queue = collections.deque()
        queue.append([rootNode, root])
        while queue:
            parent, cur = queue.popleft()
            new_root = None
            prev_root = None
            for child in cur.children:
                new_node = TreeNode(child.val)
                # 如果不是第一个孩子，那么可以设置为前一个的右孩子
                if prev_root:
                    prev_root.right = new_node
                # 是第一个孩子的话，cur 的左孩子就是第一个孩子
                else:
                    new_root = new_node
                # 更新前一个的节点
                prev_root = new_node
                # 把当前node，和对应的N叉树node 放进去，进行下一轮
                queue.append([new_node, child])
            parent.left = new_root
        return rootNode

    def decode(self, data):
        """Decodes your binary tree to an n-ary tree.
        :type data: TreeNode
        :rtype: Node
        """
        if not data:
            return None
        # bfs，把左边第一个孩子一直往右边走，边走边添加进当前node 的孩子节点
        # 因为encode 的时候，是把所有孩子都变成右孩子 除了第一个孩子
        rootNode = Node(data.val, [])
        queue = collections.deque()
        queue.append([rootNode, data])
        while queue:
            parent, cur = queue.popleft()
            child = cur.left
            while child:
                new_node = Node(child.val, [])
                parent.children.append(new_node)
                queue.append([new_node, child])
                child = child.right
        return rootNode

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))