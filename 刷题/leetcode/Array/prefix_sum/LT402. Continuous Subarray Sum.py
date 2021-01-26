class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def continuousSubarraySum(self, A):
        # write your code here
        min_prefix = 0
        left, right = -1, -1
        max_prefix = float("-inf")
        sums = 0
        min_index = -1
        for i in range(len(A)):
            sums += A[i]
            if sums - min_prefix > max_prefix:
                max_prefix = sums - min_prefix
                left = min_index + 1
                right = i
            if sums < min_prefix:
                min_prefix = sums
                min_index = i
        return [left, right]


'''
找到最大前缀和， 跟 最小前缀和 
两个相减 就是最大值
我们需要追踪最小前缀和 跟它的index

'''