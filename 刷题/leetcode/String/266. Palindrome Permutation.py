class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        count = 0
        for val in dic.values():
            if val % 2 == 1:
                count += 1
            if count > 1:
                return False
        return True
'''
这道题比较巧妙
统计所有字符出现的次数
因为如果要回文的话 
那么我们单数出现次数 的字符 只允许出现一个
那么用 count 记录 如果有字符 不能被2 整除 我们的count就+1
如果count 大于1 说明肯定不是回文

'''