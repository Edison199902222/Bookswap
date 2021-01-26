class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [-1 for i in range(2 * len(nums))]
        stack = []
        nums = nums * 2
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                result[stack.pop()] = nums[i]
            stack.append(i)
        return result[:n]
'''
因为这是一个circular array
所以我们需要两个原数组 这样才能知道每一个数组中的数字下一个大的数
然后stack 维持一个递减的数组 如果一旦遇到一个比stack顶部 大的数字
那么我们就把栈顶pop出来 把栈顶这个的index 更新成当前的数字 然后继续while循环 一直更新下去

'''