class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # 找到最多k个不一样的数的所有subarray - 最多k - 1 个不一样的数的subarray = 有k 个数的subarray
        return self.at_MostK(A, K) - self.at_MostK(A, K - 1)

    # 计算有多少个subarray 最多有k个不一样的数
    def at_MostK(self, A, k):
        counter = collections.Counter()
        left = 0
        difference = 0
        result = 0
        # 怎么算subarray呢
        # 如果在left  到 right中，没有超过 k个不一样的数
        # 那么 用right - left + 1 就是left right subarray 的个数
        # [1,2,3] left = 0， right = 2, 这说明 长度为3 的符合条件的有一个，并且长度为2 的符合条件的有一个
        # 并且长度为1 的符合条件的有1 个，总共是3个
        # 其实就是，必须带上right的有几个，然后前面也是这样计算，local -> global
        for right in range(len(A)):
            counter[A[right]] += 1
            if counter[A[right]] == 1:
                difference += 1
            # 不用left 小于right，因为最少的情况就是left = right + 1， 这时候differnece = 0
            while difference > k:
                counter[A[left]] -= 1
                if counter[A[left]] == 0:
                    difference -= 1
                left += 1
            result += right - left + 1
        return result
