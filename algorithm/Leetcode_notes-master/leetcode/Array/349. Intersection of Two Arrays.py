'''
先用比较哪个list 短 我们用短的list 作为 set
因为用短的话 比较节省空间复杂度
然后 短的list 变成set了之后
遍历长list 查 是否在短的list 的 set中
如果在的话 添加进结果里 并且在set中 pop出去这个元素 因为不能有重复元素出现
time ：O(m+n)
space ：O(min(m,n))
'''
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > nums2:
            self.intersection(nums2, nums1)
        new_set = set()
        result = []
        for i in nums1:
            new_set.add(i)
        for i in range(len(nums2)):
            if nums2[i] in new_set:
                result.append(nums2[i])
                new_set.discard(nums2[i])
        return  result

