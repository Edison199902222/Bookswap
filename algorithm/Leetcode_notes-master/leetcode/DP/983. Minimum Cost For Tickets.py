class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        # 因为当前天数的状态取决于前面 一天， 七天，三十天的，所以dp不能只记录days 中有的天数
        n = max(days)
        dp = [float('inf') for i in range(n + 1)]
        dp[0] = 0
        days = set(days)
        for i in range(1, n + 1):
            if i not in days:
                dp[i] = dp[i - 1]
            else:
                # buy one day pass
                dp[i] = min(dp[i], dp[i - 1] + costs[0])
                if i >= 7:
                    dp[i] = min(dp[i], dp[i - 7] + costs[1])
                # 有可能七天的票比一天的便宜,因为i不足7天，所以七天内 只需要花费七天pass的钱
                else:
                    dp[i] = min(dp[i], costs[1])
                if i >= 30:
                    dp[i] = min(dp[i], dp[i - 30] + costs[2])
                    # 和七天的同理
                else:
                    dp[i] = min(dp[i], costs[2])
        return dp[n]


'''
创建一个dp 数组 dp[i]表示 我们用最少钱可以到的第i天
首先把第0位设置成0 因为第0 位我们并不使用 
然后把days 变成一个set 方便查找
从第一天遍历到 最后一天
如果当前天数 并不是我们会旅游的天数 那么 它的钱 跟前一天的钱是一样的
如果 当前天数 是旅游天数 那么有三种情况
第一种情况 我们买一天的票，那么我们就是由能达到前一天花的最少钱 加上一天票的钱 
第二种情况， 如果当前天数大于7 的话 那么我们可以由到达七天前花的最少钱的 加上七天票的钱 
如果不大于7 的话 我们也可以这一天单独买七天的票 因为有可能七天的票比一天票便宜
第三种情况 如果当前天数 大于30 的话， 那么我么可以由到达三十天前画的最少钱 加上30天票钱 
如果小于30 我们也可以单独买 30 天的票 为有可能30天的票比一天票便宜
'''