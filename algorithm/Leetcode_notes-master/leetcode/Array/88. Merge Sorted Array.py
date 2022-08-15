'''
这道题是从尾部开始比较
双指针
两个指针放在两个list尾部
如果list2 大于 list1 则把list2 元素放在list1 尾部 然后移动list2
如果list2 小于 list1 则把list1 的尾部元素 和 当前list1的元素进行交换 移动list1
最后要检查 list2 是不是动完了
如果没有完了话 就把list1的前n个元素 等于list2 的n个元素 因为这样说明 list1的所有元素比list2的大 list1前面n个元素都是0
'''

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums2[n - 1] > nums1[m - 1]:
                nums1[m + n -1] = nums2[n - 1]
                n -= 1
            else:
                nums1[m + n - 1], nums1[m - 1] = nums1[m - 1], nums1[m + n -1]
                m -= 1
        if m == 0 and n > 0:
            nums1[:n] = nums2[:n]