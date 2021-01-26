'''
创建两个字典
用两个loop 去把这两个字符串 放进去
每出现一次 就+1
最后看看两个字典是不是一样
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1,dic2 = {},{}
        for i in s:
            dic1[i] = dic1.get(i,0)+1
        for i in t:
            dic2[i] = dic2.get(i,0)+1
        return dic1 == dic2