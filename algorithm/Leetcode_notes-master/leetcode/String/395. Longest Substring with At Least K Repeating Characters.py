'''
可以分段来处理
先用字典 把每一个字母出现的次数写上去
然后 我们找到s 中第一个不满足k times的字母
切割开来 我们把 不满足的字母 之前的那些字符串 去找
不满足字母 后面的字符串再找
'''


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        dic = {}
        for i in range(s):
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        fullstring = True
        for i in range(s):
            if dic[i] < k:
                fullstring = False
        if fullstring == True:
            return len(s)
        begin, end, result = 0, 0, 0
        while end < len(s):
            if dic[s[end]] < k:
                result = max(result, self.longestSubstring(s[begin:end], k))
                begin = end + 1
            end += 1
        result = max(result, self.longestSubstring(s[begin:end], k))
        return result