# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidSequence(self, root, arr):
        """
        :type root: TreeNode
        :type arr: List[int]
        :rtype: bool
        """
        return self.helper(root, arr, 0)

    def helper(self, root, arr, index):
        if not root or index >= len(arr) or root.val != arr[index]:
            return False
        if (not root.left) and (not root.right) and index == len(arr) - 1:
            return True
        return self.helper(root.left, arr, index + 1) or self.helper(root.right, arr, index + 1)
'''
利用index 去操作
每一次递归 
base case ：如果发现 root 是 none 或者 index 超过 数组的最大index 时 或者 当前root value 不等于数组的元素时
我们就return false
如果 发现 没有左孩子 没有右孩子 并且 index 正好是 array 的最后一位时 
说明我们找到正确的路径了 return true
最后 每一次递归我们需要返回 左边的 跟 右边 的true 或者 false 值 传递到上面去
'''