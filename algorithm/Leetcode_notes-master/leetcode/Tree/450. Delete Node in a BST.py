# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        elif key > root.val:
            # 如果key在右边，说明右边要delete 一个node
            root.right = self.deleteNode(root.right, key)
            return root
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        else:
            left = root.left
            right = root.right
            if left is None:
                return right
            elif right is None:
                return left
            else:
                temp = right
                # 找到右子树中 最左边的node 把left 链接到 最左的node
                while right.left:
                    right = right.left
                # 删除当前root之后，左边的子树自动变成右边子树最小的node的左边
                right.left = left
                # 把之前的right 当成root return 上去
                return temp
'''
如果要删除 树里面一个node 的时候
我们把它删除后， 如果左边 跟 右边都是有node 的情况下。 需要把它的右边节点当成新的root
把旧root的左边节点 放到 右边子树的 最左节点的左边
如果左边没有node， 那就直接return 右边就好
右边没有 如果左边就好
'''