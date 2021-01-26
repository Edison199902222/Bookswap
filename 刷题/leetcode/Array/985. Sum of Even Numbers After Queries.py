class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        result = 0
        result_list = []
        for i in A:
            if i % 2 == 0:
                result += i
        for i in (queries):
            temp_val, temp_index = i[0], i[1]
            prev = A[temp_index]
            A[temp_index] += temp_val
            if prev % 2 == 0:
                result -= prev
            if A[temp_index] % 2 == 0:
                result += A[temp_index]
            result_list.append(result)
        return result_list
'''
先把所有A数组中 所有为偶数的数字加起来 计算总和 计为result
然后遍历queries 我们需要用prev变量 去得到需要改变数字的index 的当前数字
然后看需要更改的那个index 的数字 也就是prev 是不是 偶数
如果是偶数 那么我们的 result 需要减去这个数字 因为 这个数字会改变 我们不知道改变后的数字是不是偶数
然后再确定 更改后的数字是不是偶数 如果是偶数 result 加上即可
'''