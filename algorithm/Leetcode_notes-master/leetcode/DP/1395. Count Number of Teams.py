class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        result = 0
        n = len(rating)
        for i in range(n):
            left = 0
            right = 0
            for l in range(i):
                if rating[l] < rating[i]:
                    left += 1
            for r in range(i + 1, n):
                if rating[r] > rating[i]:
                    right += 1
            result += (left * right) + (i - left) * (n - i - 1 - right)
        return result
'''
我们可以寻找每一个数的左边 跟 右边
左边 代表 当前数字 i 的左边有多少个数字比自己小
右边表示 当前数字的右边有多少个数字比自己大
然后 找出来之后
我们就可以更新 结果 
每次从左边抽取一个 右边抽一个 组成三个 left < i < right
这样就会有 left * right 个subset
然后 我们还要找当前数字 i 有没有可能组成 left > i > right的组合
所以 左边 比自己大的数量 就是用 自己的idnex  i - 左边有多少个数字比自己小
右边比自己小的数字的数量 就是用 数组总共的数量 - i - 1 代表 右边有几个数字
然后再用 右边有几个数字 减去 右边比自己大数字的数量 就是右边比自己小的数量
(i - left) * (n - i - 1 - right) 代表满足 left > i > right所有组合
然后再加起来 (left * right) + (i - left) * (n - i - 1 - right)
'''