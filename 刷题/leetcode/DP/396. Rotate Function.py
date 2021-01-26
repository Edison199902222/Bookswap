class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        sums = sum(A)
        arr_product = 0
        for i in range(len(A)):
            arr_product += i * A[i]
        max_val = arr_product
        for i in range(1, len(A)):
            arr_product = arr_product + sums - len(A) * A[-i]
            max_val = max(max_val, arr_product)
        return max_val
'''
假如：[4,5,3,2,9]
F(0) = 4 * 0 + 5 * 1 + 3 * 2 + 2 * 3 + 9 * 4 = 53
F(1) = 4 * 1 + 5 * 2 + 3 * 3 + 2 * 4 + 9 * 0 = 31
我们从上面的规律可以知道 F(1) 是由 F(0) 除了最后一个index 数字9 以外， 其他的所有数字都加了一个自己
然后再减去最后一个index 就可以
总结一下，f(n) = f(n - 1) + 自身的sum 然后再减去 最后一个数字 * 数组的长度 

'''