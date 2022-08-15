# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        max_val = max(nums)
        index = nums.index(max_val)
        node = TreeNode(max_val)
        node.left = self.constructMaximumBinaryTree(nums[:index])
        node.right = self.constructMaximumBinaryTree(nums[index + 1:])
        return node
'''
利用递归 
先找到最大值 跟 最大值的index 时间复杂度是 O(n)
然后 用切片 把最大值左边作为列表 递归 左子树
右边也一样操作
Time complexity: O(nlogn) ~ O(n^2)

Space complexity: O(nlogn) ~ O(n^2) 
'''