import collections


class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        max_number = collections.deque()
        min_number = collections.deque()
        left = 0
        result = float("-inf")
        for right in range(len(nums)):
            while max_number and nums[right] > max_number[-1]:
                max_number.pop()
            while min_number and nums[right] < min_number[-1]:
                min_number.pop()
            max_number.append(nums[right])
            min_number.append(nums[right])
            if max_number[0] - min_number[0] > limit:
                if nums[left] == max_number[0]:
                    max_number.popleft()
                if nums[left] == min_number[0]:
                    min_number.popleft()
                left += 1
            result = max(result, right - left + 1)
        return result


class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        max_number = collections.deque()
        min_number = collections.deque()
        left = 0
        result = float("-inf")
        for right in range(len(nums)):
            while max_number and nums[right] > max_number[-1]:
                max_number.pop()
            while min_number and nums[right] < min_number[-1]:
                min_number.pop()
            max_number.append(nums[right])
            min_number.append(nums[right])
            while left <= right and max_number[0] - min_number[0] > limit:
                if nums[left] == max_number[0]:
                    max_number.popleft()
                if nums[left] == min_number[0]:
                    min_number.popleft()
                left += 1
            result = max(result, right - left + 1)
        return result


'''
维护两个deque， slicing window + deque
数组每个数都是正整数， 最长的话 就是整个数组的长度， 所以我们把left 尝试放到数组第一位
第一个维持住最大值
第二个维持住最小值 #一般deque 维护，都是用while循环
然后 我们只需要遍历一遍 用左右两个指针 去移动， 右边指针每次移动一格， 
如果发现新进来的元素 使得我们的limit 不合法了 也就是如果改变了最大值或者最小值的话，我们就移动左指针
为什么移动左指针， 是因为， 如果继续移动右指针的话， 右边指针如果不影响最大最小值的话，那么limit还是不合法，
如果影响了最大值的话那么最大值会变得更大，减去最小值还是不合法， 如果影响最小值，最小值变得更小， limit还是不合法，所以我们要
移动左指针，去尝试能不能使得最大值变得更小， 或者使得最小值变得更大
移动左指针时 我们需要检查 两个deque 如果移动的那个指针是影响我们最大或者最小值的 那么我们就得把最大或者最小值剔除
'''