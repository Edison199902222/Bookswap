'''
把两个加在一起 当作two sum的问题
A + B 之后 把他放进一个字典中
C + D 之后 也放进一个字典中
然后check 第一个字典 看看 有没有对应的值在字典2 中
'''

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        dic1 = {}
        dic2 = {}
        for i in A:
            for j in B:
                if i+j in dic1:
                    dic1[i+j] += 1
                else:
                    dic1[i+j] = 1
        for i in C:
            for j in D:
                if i + j in dic2:
                    dic2[i + j] += 1
                else:
                    dic2[i + j] = 1
        count = 0
        for i in dic1:
            if -i in dic2:
                count += dic1[i] * dic2[-i]
        return count
