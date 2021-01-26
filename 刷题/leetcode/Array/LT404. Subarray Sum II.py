class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """
    def subarraySumII(self, A, start, end):
        n = len(A)
        right_start, right_start_sum = 0, 0
        right_end, right_end_sum = 0,0
        result = 0
        for i in range(n):
            right_start = max(i, right_start)
            right_end = max(i, right_end)
            while right_start < n and right_start_sum + A[right_start] < start:
                right_start_sum += A[right_start]
                right_start += 1
            while right_end < n  and right_end_sum + A[right_end] <= end:
                right_end_sum += A[right_end]
                right_end += 1
            if right_end - right_start > 0 :
                print(right_end,right_start)
                result += right_end - right_start
            if right_start > i:
                right_start_sum -= A[i]
            if right_end > i:
                right_end_sum -= A[i]
        return result
'''
O(N) 的两根指针的算法

其实需要三根指针, 因为需要额外记录一下从哪个位置开始的加和已经 >= start 了.

对于每一个左端点 left, 求出对应的两个右端点 right_start, right_end. 前者表示最左边的使得 [left, right_start] 子数组的和不小于 start 的点, 而后者表示最右边的使得 [left, right_end] 子数组的和不大于 end 的点.

right_end - right_start + 1 就是以 left 为左端点的合法子数组的数量.

从左到右枚举 left, 而 right_start, right_end 随着left的增长也是只增不减的, 所以时间复杂度是 O(N)
'''