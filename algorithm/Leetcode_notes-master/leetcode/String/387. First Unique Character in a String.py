'''
用一个hash table 去遍历 然后把字符串的每个字母 跟他出现的次数add 进去
再用一次遍历 去检查 哪个出现的次数是等于1
'''

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]]+=1
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1