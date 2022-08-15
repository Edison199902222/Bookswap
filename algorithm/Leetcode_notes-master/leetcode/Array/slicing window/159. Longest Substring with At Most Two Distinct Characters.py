class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = collections.Counter()
        counter = 0
        result = 0
        left = 0
        for right in range(len(s)):
            dic[s[right]] += 1
            if dic[s[right]] == 1:
                counter += 1
            while counter >= 3:
                dic[s[left]] -= 1
                if dic[s[left]] == 0:
                    counter -= 1
                left += 1
            result = max(result, right - left + 1)
        return result
'''
跟76题一样
问题 为什么 每一次right 移动完之后 不需要初始化left呢
是因为， 我们right一直在增大
对于下一个right而言，它的窗口是包括当前的right的，
如果对于当前right来说， 当前left 之前的index 和right 组成的窗口 不满足题目条件的话
那么对于下一个right而言 同样不会满足，所以没有必要left 初始化
'''