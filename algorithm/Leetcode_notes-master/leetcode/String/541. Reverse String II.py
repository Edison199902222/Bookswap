class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        list_s = list(s)
        left = 0
        right = len(s) - 1
        for i in range(0, len(list_s), 2 * k):
            left = i
            right = min(i + k - 1, len(s) - 1)
            while left < right:
                list_s[left], list_s[right] = list_s[right], list_s[left]
                left += 1
                right -= 1
        return "".join(list_s)
'''
题目意思是
先反转 k 个字符 然后 每间隔 2k个 反转k个字符
所以 我们先把s 变成list
然后 每隔 2k 利用同向双指针 去翻转
最后合并
'''