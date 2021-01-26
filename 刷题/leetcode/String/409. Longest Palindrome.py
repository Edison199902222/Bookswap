class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = collections.Counter(s)
        is_odd = False
        count = 0
        for i in dic.values():
            if i % 2 != 0:
                is_odd = True
            count += (i // 2)*2
        if is_odd:
            count += 1
        return count
'''
首先统计 s
然后设置一个 is odd 用来判断里面有没有出现奇数次数的字符
然后遍历字典
对于每个字符出现的次数
看是不是偶数
如果不是的话 设置 is odd
同时 我们开始计算数量 把每个字符出现的次数 // 2 代表 除2 后向下取整 一定是一个 偶数！

'''