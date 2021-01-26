import bisect


class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        jobs = []
        for i in range(len(startTime)):
            start = startTime[i]
            end = endTime[i]
            money = profit[i]
            jobs.append((start, end, money))
        # 对end 排序
        # 1. 是为了贪心，end时间结束越早，更小可能与后面产生overlap
        # 2. 为了待会利用start time 找寻不overlap的区间
        jobs = sorted(jobs, key=lambda x: x[1])
        # dp[i][j], i means end time
        # j means profit
        dp = [[0, 0]]
        # 遍历jobs，end 时间结束越早我们先遍历 贪心思想，因为它有可能产生的利润越多
        for start, end, money in jobs:
            # 利用二分找到 start 的upeer bound， 这是在dp 里面 最接近start 的end time
            # 因为end time 有可能一样，所以我们要在end time 一样时， index 越大越好， 因为index 越大 它的profit 越大
            index = bisect.bisect(dp, [start + 1]) - 1
            # 找到当前start time 之前可以产生的最大的profit 的之后，我们选择 当前是不是需要take 这份工作
            # 如果比dp 最后一位，也就是profit 最大的 产生的利润还要多，那么就take
            if dp[index][1] + money > dp[- 1][1]:
                dp.append([end, dp[index][1] + money])
        return dp[-1][1]
