class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        # write your code here
        result = 0
        S.sort()
        for i in range(2, len(S)):
            left = 0
            right = i - 1
            while left < right:
                sums = S[left] + S[right]
                if sums > S[i]:
                    result += right - left
                    right -= 1
                else:
                    left += 1
        return result
'''
首先对长度排序
枚举最大的边i 然后 枚举次大的边 right
最小的边 left 单调递增
所以 我们检查 left 跟 right 此时是不是 大于 最大的边 i

如果大于的话，那么 直接 right - left 加进结果， 这个就相当于 left 一直移动到right - 1， 因为left 是递增的， 所以一直到right - 1 肯定都是大于i的
然后 right - 1， 去尝试 更小的right 可不可以满足 条件

为什么 right - 1 以后， left 不用初始化呢， 是因为，我们已经算出刚好这时候的left + right 大于i，说明 之前的left -1， left -2 是不能满足这个条件的
现在right 要变小，如果left 初始化的话，那么肯定不能满足 大于i的条件的！！！right 跟 left 都变小 肯定不能满足

如果 小于 i的话， 那么left 需要增加
'''