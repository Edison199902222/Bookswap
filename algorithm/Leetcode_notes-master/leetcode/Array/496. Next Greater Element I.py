class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums1:
            index = nums2.index(i)
            flag = False
            for j in range(index + 1, len(nums2)):
                if nums2[j] > i:
                    flag = True
                    res.append(nums2[j])
                    break
            if not flag:
                res.append(-1)
        return res
'''
用stack 跟 字典
字典中储存 num2 每一个元素对应的 在之后的最大值
然后遍历数组1
看看每一个元素 是否在字典中有对应的最大值 没有的话直接添加 -1
'''
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        dic, stack = {}, []
        for i in nums2:
            while stack and i > stack[-1]:
                dic[stack.pop()] = i
            stack.append(i)
        res = []
        for x in nums1:
            if x in dic:
                res.append(dic[x])
            else:
                res.append(-1)
        return res
