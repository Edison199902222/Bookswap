class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        index_list = []
        result = []
        for i, nums in enumerate(matrix):
            for j, value in enumerate(nums):
                if i + j >= len(index_list):
                    index_list.append([])
                index_list[i + j].append(value)
        for index, value in enumerate(index_list):
            if index % 2 == 0:
                result += value[::-1]
            else:
                result += value
        return result



'''
有点跟8皇后问题像
我们把 找出规律
每一个格子 都会属于 i + j
比如 0 0 这个格子 它就属于 0 + 0 = 0 这个里面
比如 0 1 跟 1 0 它们共同属于 0 + 1 = 1 里面
所以 我们可以把 同一条斜线上面的规律 总结为 如果在同一条线上的格子 那么它们的i + j 肯定相同
所以 我们建立一个 list
它的index 作为 我们的key 对应 同一条线上的所有元素
然后 我们发现 规律 如果 这一条线是奇数的话 那么他的顺序是从左下到右上的
如果是偶数的话 顺序是从右上到左下的 
'''
