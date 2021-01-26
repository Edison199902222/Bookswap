'''
题意是找出给出字符串里面，连续10个字母出现多次的串。
首先想到的是一重循环，然后用字典储存每个串出现的次数，最后找出值大于1的key。
'''

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = {}
        result = []
        for i in range(len(s)-9):
            chart = s[i:i+10]
            if chart not in dic:
                dic[chart] = 1
            else:
                dic[chart]+=1
        for key in dic:
            if dic[key] > 1:
                result.append(key)
        return result

