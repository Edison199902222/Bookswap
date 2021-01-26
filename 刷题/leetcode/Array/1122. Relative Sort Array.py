import collections
'''
先用字典 把arr1 中出现的字符 和 次数存进去
然后遍历array2 每个当前的字符 乘以 在arr1 出现的次数 加进res中 顺便把已经出现了的 pop出来
然后 res + 排序好的字典
sorted 可以把目前变成排序好的list 
elements 可以把字典中的元素弄出来 
'''

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        dic = collections.Counter(arr1)
        res = []
        for i in arr2:
            res += [i] * dic.pop(i)
        return res + sorted(dic.elements())

