class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        if len(stoneValue) < 2:
            return 0
        self.memo = {}
        self.presum = [0 for i in range(len(stoneValue) + 1)]
        # 用presum 做预处理
        for i in range(1, len(stoneValue) + 1):
            self.presum[i] += self.presum[i - 1] + stoneValue[i - 1]
        return self.dfs(0, len(stoneValue) - 1, stoneValue)

    def dfs(self, start, end, stone):
        if start == end:
            return 0
        if start >= end:
            return 0
        if start + 1 == end:
            return min(stone[start], stone[end])
        if (start, end) in self.memo:
            return self.memo[(start, end)]
        result = 0
        # 区间dp，尝试去分成left，和 right
        for i in range(start, end):
            cur_result = 0
            # 得到left 的sum
            # i + 1 在presum 中等于 start 到 i 的sum 减去 start 前面一个的sum
            left = self.presum[i + 1] - self.presum[start]
            # 得到right 的sum
            # end + 1 代表 start 到 end 的sum， 减去 i + 1 在presum 代表 start 到 i 的sum
            right = self.presum[end + 1] - self.presum[i + 1]
            # 判断哪一个更小
            if left < right:
                cur_result += self.dfs(start, i, stone)
                cur_result += left
            elif left > right:
                cur_result += self.dfs(i + 1, end, stone)
                cur_result += right
            else:
                cur_result = max(self.dfs(start, i, stone), self.dfs(i + 1, end, stone))
                cur_result += left
            result = max(cur_result, result)
        self.memo[(start, end)] = result
        return result