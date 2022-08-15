class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        # 第一步 看有没有右子树，有的话， 寻找右边子树最左node
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        # 没有右子树，找到把当前node 所处于的左子树的父节点
        # 因为要找比node大一些的，需要找到让自己在左子树的parent
        while node.parent and node.parent.right is node:
            node = node.parent
        return node.parent