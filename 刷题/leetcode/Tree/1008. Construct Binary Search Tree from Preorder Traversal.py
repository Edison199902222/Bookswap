# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
第一种方法是用二分查找 加上递归
核心思想就是， 每次递归 我们有两个 变量 low high 代表数组中我们可以选取数字的边界
如果 low 等于 high 说明没有数字可以选择 直接return
然后 我们把 数组中 第一个数字 也就是我们的左边接 low 设置为root
二叉搜索树的特点就是 左边所有数 都小于root
我们利用二分查找（这个函数会从数组中查找 如果数组中没有比它大的数字 那么会返回最后一个index， 如果有的话，会返回比它大的数字左边的index）
 从low + 1 到 high 也就是右边界 找到 数组中 哪些数字是小于我们root的 返回一个index
 比如【1，2，3】target = 4 我们就会返回index 3
 然后 这个index 设置成我们的右边边界 lo + 1 设置成我们左边边界 作为我们左孩子递归下去
 mid 到 high 设置成我们 右孩子的两个边界 递归下去
 复杂度是 nlogn
'''
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def helper(lo, hi):
            if lo == hi:
                return None
            root = TreeNode(preorder[lo])
            mid = bisect.bisect(preorder, preorder[lo], lo + 1, hi)
            root.left = helper(lo + 1, mid)
            root.right = helper(mid, hi)
            return root

        return helper(0, len(preorder))
'''
这个方法 O n
我们设置一个全局变量i 来track 我们在数组中当前需要设置的位置
设置一个bound 参数， 代表 每一层 设置的value 不能超过这个bound， 超过了这个bound就是不对了 
一般设置 root 的value给左孩子 作为bound， 因为左孩子的value 不能超过root
数组中第一个数就是root 所以首先把 i 设置成root
然后i + 1 
把 root 设置为bound 递归下去 设置为左孩子
结束后 i 会等于一个 比root 大的一个值 的index
然后再把 bound不变 递归下去 作为右孩子 
最后返回 root
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.i = 0
    def bstFromPreorder(self, preorder, bound = float("inf")):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if self.i == len(preorder) or preorder[self.i] > bound:
            return None
        root = TreeNode(preorder[self.i])
        self.i += 1
        root.left = self.bstFromPreorder(preorder, root.val)
        root.right = self.bstFromPreorder(preorder, bound)
        return root