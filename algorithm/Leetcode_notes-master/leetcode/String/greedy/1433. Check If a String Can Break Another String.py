class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        s1 = sorted(s1)
        s2 = sorted(s2)
        flag1 = True
        flag2 = True
        for i in range(len(s1)):
            if ord(s1[i]) < ord(s2[i]):
                flag1 = False
            if ord(s2[i]) < ord(s1[i]):
                flag2 = False
        return flag1 or flag2
'''
利用了greedy
因为数据量太大 所以我们不能用dfs
我们排序好两个字符串
找 一个字符串 中的每一个元素 是不是在另一个字符串中 都有比它大的元素
'''