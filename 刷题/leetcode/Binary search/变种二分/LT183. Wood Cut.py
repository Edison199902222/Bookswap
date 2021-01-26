class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """

    def woodCut(self, L, k):
        # write your code here
        if not L:
            return 0
        left, right = 1, max(L)
        while left + 1 < right:
            mid = (left + right) // 2
            if self.count(L, mid) >= k:
                left = mid
            else:
                right = mid
        if self.count(L, right) >= k:
            return right
        elif self.count(L, left) >= k:
            return left
        return 0

    def count(self, L, length):
        pieces = 0
        for i in L:
            pieces += i // length
        return pieces
'''
首先 木头的长度范围是至少是1 最大可以到 L的最大值， 因为如果k = 1 的话 我们只需要一根木头， 那么我们就取L 的最大值作为长度就行了
然后用二分法，调用一个计算 以当前长度算出有多少根木头的函数， 如果以mid 作为长度 算出来的木头大于等于 k 根，那么我们可以尝试把木头的长度变长一些， left = mid
如果算出来的木头 小于 k根 那么我们可以尝试把木头的长度变短一些，这样可以有更多的木头， right = mid
最后先检查end作为长度 是不是 大于k根 
为什么先算 end呢，因为我们在保证至少k根下 需要长度越长越好
'''