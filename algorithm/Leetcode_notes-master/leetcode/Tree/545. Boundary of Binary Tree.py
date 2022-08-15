# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # 思路， left boundary 需要找到左子树最左的node， 并且要避免添加叶子节点，因为helper2 会添加一遍叶子节点
    # helper2 把所有叶子节点添加进result，注意不要添加root了，因为root已经有了
    # helper3 right boundary 需要找到右子树最右的node，但是 方向要逆转，所以应该最后添加进result
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.result = [root.val]
        self.root = root
        self.helper(root.left)
        self.helper2(root)
        self.helper3(root.right)
        return self.result

    def helper(self, root):
        # 不添加叶子节点
        if not root or (not root.left and not root.right):
            return
        # 先添加进result
        self.result.append(root.val)
        if root.left:
            self.helper(root.left)
        else:
            self.helper(root.right)

    def helper2(self, root):
        if not root:
            return
        self.helper2(root.left)
        # 不能添加root， 避免重复
        if root != self.root and not root.left and not root.right:
            self.result.append(root.val)
            return
        self.helper2(root.right)

    def helper3(self, root):
        # 不添加叶子节点，避免重复
        if not root or (not root.left and not root.right):
            return
        if root.right:
            self.helper3(root.right)
            # 满足逆向
            self.result.append(root.val)
        else:
            self.helper3(root.left)
            self.result.append(root.val)
        return

