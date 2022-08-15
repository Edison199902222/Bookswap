class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if K == len(A):
            return len(A)
        # 维持一个窗口，只需要里面的k值大于等于0
        # 如果小于0，说明窗口太大了，不能承受，那么left 往右移动
        # subarray是利用滑动窗口的好机会 正好题目的要求有一点单调性质 更长的subarray一定需要翻转的更多
        left = 0
        result = 0
        for right in range(len(A)):
            if A[right] == 0:
                K -= 1
            while left <= right and K < 0:
                if A[left] == 0:
                    K += 1
                left += 1
            result = max(result, right - left + 1)
        return result

    class Solution:
        def longestOnes(self, A: List[int], K: int) -> int:
            # 也可以用prefix sum 做，这里的prefix是记录的是当前区间内，有几个0
            # 如果prefix 大于k了，那么检查 prefix - k 有没有在之前出现过，有的话，减去
            # 比如，prefix = 4， k = 3， 意思是当前区间内有4 个0， 那么我要剔除 4 - 3 = 1 一个0，
            # 所以找，之前区间内有没有一个区间是只有一个0的，有的话，去掉这个，后半部分就是答案
            number_zero = 0
            dic = collections.defaultdict(int)
            result = 0
            for i in range(len(A)):
                if A[i] == 0:
                    number_zero += 1
                if number_zero <= K:
                    result = max(result, i + 1)
                else:
                    if number_zero in dic:
                        result = max(result, i - dic[number_zero - K])
                if number_zero not in dic:
                    dic[number_zero] = i
            return result