class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        m = len(nums)
        # dp[i][j]意思是 从nums i 到j 中戳破所有气球能得到的最大分数
        dp = [[0] * (m + 1) for i in range(m + 1)]
        # 小于三个气球是得不到分的，所以lenggth 为3开始
        for length in range(3, m + 1):
            # 找到开始位置，跟最多能到哪个位置作为开始
            for i in range(1, m - length + 2):
                j = i + length - 1
                # 选取最后一个戳爆的气球
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i - 1] * nums[j - 1] * nums[k - 1])

        return dp[1][m]
'''
先初始化 把数组 前后加上1
然后建立一个 dp 二维数组 
dp[left][right]表示 从left 到 right 这么多的距离 戳破气球可得到最大的值
然后 我们先循环
第一重循环 目的是 为了扩大 left gen right之间的距离 
第二重循环 是为了得到 left指针
然后 right = left 指针 加上 他们两个的距离 
第三个循环 我们枚举 left right 之间 每一个气球 都有可能被戳破 并且加上 第i个 就是被戳破的最后一个气球
如果是被戳破的最后一个气球 那么 left 到 right之间 最大值就会是 
left 乘 i 乘 right 的值 加上 之前 从left 到 i 被戳破的最大值 加上之前 i 到right 被戳破的最大值
'''