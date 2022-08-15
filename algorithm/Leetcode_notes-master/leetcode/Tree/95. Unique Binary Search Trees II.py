# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
两个题目均可以通过递归实现，思路如下：
1）遍历[1,n]中每个整数,并将正在遍历的整数 i 设为根节点
2）将 [1,i-1] 的整数构建出来的子树作为整数 i 构建的根节点的左子树，将 [i+1,n] 的整数构造出来的子树作为整数 i 构建的根节点的右子树
3）对得到的左右子树进行组合，这样便可得到以整数i为根节点的所有二叉树
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0: return []
        return self.helper(1, n)

    def helper(self, start, end):
        if start > end:
            return [None]
        result = []
        for root_value in range(start, end + 1):
            # 可以构成左边子树的 node 组成的列表
            left = self.helper(start, root_value - 1)
            # 可以构成右边子树的 node 组成的列表
            right = self.helper(root_value + 1, end)
            for i in left:
                for j in right:
                    # 枚举左 右子树
                    # root 一定要放在里面，才会不断创建新root， 不然旧root 的左右一直再更新
                    root = TreeNode(root_value)
                    root.left = i
                    root.right = j
                    result.append(root)
        return result

