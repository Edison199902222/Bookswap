# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        list_node = []
        list_val = []
        self.inorder(root, list_node, list_val)
        list_val.sort()
        for i in range(len(list_val)):
            list_node[i].val = list_val[i]
        return root

    def inorder(self, root, list_node, list_val):
        if not root:
            return
        self.inorder(root.left, list_node, list_val)
        list_node.append(root)
        list_val.append(root.val)
        self.inorder(root.right, list_node, list_val)
'''
inorder遍历取到数组里，对数组排序之后按顺序将排序后的值赋回给节点
'''

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 中序遍历 会形成有序的顺序
        stack = []
        first = second = prev = None
        while stack or root:
            # 中序遍历， 利用stack 递归到左边
            while root:
                stack.append(root)
                root = root.left
            # 检查， 如果前一个节点的值大于当前节点，错误的节点找到
            # 更新frist 以及 second
            root = stack.pop()
            if prev != None and prev.val > root.val:
                if first == None:
                    first = prev
                    second = root
                # 第二次找到错误节点， 只需要把second 更新成root， 最后交换
                else:
                    second = root
                    break
            prev = root
            root = root.right
        first.val, second.val = second.val, first.val