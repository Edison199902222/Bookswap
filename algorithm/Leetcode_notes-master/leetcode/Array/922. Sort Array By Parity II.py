'''
创建一个新的list
然后创建两个指针 一个指向even index 一个指向odd index
遍历旧list 如果当前数字是odd 就让他等于新list的odd 指针
如果当前是even 就让他等于新的list even指针
'''

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = [0 for i in range(len(A))]
        even_pointer = 0
        odd_pointer = 1
        for i in range(len(A)):
            if A[i] % 2 == 0:
                res[even_pointer] = A[i]
                even_pointer += 2
            else:
                res[odd_pointer] = A[i]
                odd_pointer += 2
        return res