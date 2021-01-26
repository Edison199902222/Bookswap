import collections

'''
对于每一个right而言， 我们找满足条件的left （left 必须小于等于right）
形成的一个窗口， 窗口里面全是repeating character
'''
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        # caculate letter fruenqency within windows
        count = collections.Counter()
        # the max letter fruenqency value
        max_val = 0
        result = 0
        for right in range(len(s)):
            count[s[right]] += 1
            max_val = max(max_val, count[s[right]])
            while left < right and right - left + 1 - max_val > k:
                count[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result
'''
核心思想是
维持一个window， 在这个window 中 我们有一个count， 来计算window中 各个字符出现了几次
max_val 维持的是在这个window中 出现次数最多字母的次数
所以， 我们每一次只需要移动right， 去检查当前window中 整个window 的长度 减去出现最多的次数的值， 判断 是否大于k
如果大于k 说明我们整个window 不能全部变成连续的子串，那么我们就移动左指针
如果不大于k， 说明这个window是合法的， 不移动左指针 
更新 result

内层循环中 用while 跟 用if效果是一样的
为什么用if 可以呢
是因为我们每一次都检查了 left指针合不合格，对于 这一次不合格的话 上一次是合格的话，因为我们right指针每一次只走了一步，所以left也只需要走一步就可以变成合格的了 
'''

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        # caculate letter fruenqency within windows
        count = collections.Counter()
        # the max letter fruenqency value
        max_val = 0
        result = 0
        for right in range(len(s)):
            count[s[right]] += 1
            max_val = max(max_val, count[s[right]])
            if right - left + 1 - max_val > k:
                count[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result