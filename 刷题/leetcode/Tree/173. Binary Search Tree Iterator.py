# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
heper函数是把自己先放进stack中 再把左节点全部放到stack中
next 是 每次pop stack中最后一个元素 这个元素就是目前最小的
然后并且添加 这个元素的右边节点 因为有点像中序遍历 左边最小 然后是中间 然后是右边
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root != None:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        node = self.stack.pop()
        current = node
        if current.right != None:
            current = current.right
            while current != None:
                self.stack.append(current)
                current = current.left
        return node.val
    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.stack

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.next_item = None
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.next_item is None:
            self.hasNext()
        temp, self.next_item = self.next_item, None
        return temp

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.next_item is not None:
            return True
        if self.stack:
            node = self.stack.pop()
            self.next_item = node.val
            if node.right:
                node = node.right
                while node:
                    self.stack.append(node)
                    node = node.left
            return True
        return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()