# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 指向的是上一层的root，这一层会变成右节点
        prev_root = None
        # 指的是上一层的right，这一层会变成左节点
        prev_right = None
        cur = root
        while cur:
            # 先得到当前层的左右节点，防止后面被改变
            temp1 = cur.left
            temp2 = cur.right
            # 更显当前层的左右层
            cur.left = prev_right
            cur.right = prev_root
            # 更新
            prev_right = temp2
            prev_root = cur
            cur = temp1
        return prev_root


'''
题目的意思可以理解为 如果有右边节点 那么一定会有左边节点
找到最左边的节点 然后 我们return最左边节点
然后在上一层 我们要做的事情就是， 把右边孩子 设置为 左边孩子的左节点
把自己 设置为 左孩子的右边节点
然后把自己的左 右孩子 设置为None
然后 我们再return 最左边的节点

'''