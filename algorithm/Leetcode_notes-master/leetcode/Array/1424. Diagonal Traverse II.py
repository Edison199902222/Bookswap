class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        index_list = []
        for i, num in enumerate(nums):
            for j, value in enumerate(num):
                if i + j >= len(index_list):
                    index_list.append([])
                index_list[i + j].append(nums[i][j])
        result = []
        for i in index_list:
            temp = i[::-1]
            result += temp
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
我们遍历array 对于每一个格子， 因为每一个格子 最多比前一个格子 的i + j 大1， 所以如果我们发现 当前格子的 i + j 大于我们的数组的话 我们就需要添加一个index 来维持
最后 因为先添加进去的元素其实在后面的 所以我们要反转输出一下

'''
