class Solution(object):
    def palindromePartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        m = len(s)
        # dp[i][k] 意思是 前i 个元素 分成 k个， 每一段都是回文的最小change
        dp = [[float("inf")] * (k + 1) for i in range(m + 1)]
        dp[0][0] = 0
        # 枚举前 i 个元素
        for i in range(1, m + 1):
            # 枚举 分成 k 个
            for K in range(1, min(i, k) + 1):
                # 找寻最后一个区间的开始位置，最小需要从k 开始找，不能比k 小
                # 因为 比如k = 2， 如果从1开始找的话，变成 前1 个元素 要形成 2 个区间， 这样是不合法的
                for j in range(K, i + 1):
                    # 找到j以后，意思是j 到 i 作为最后一个区间， dp[j - 1][K - 1] 意思是前j - 1 个元素形成的 k - 1 个区间
                    # 两个加起来 就可以形成k个区间
                    dp[i][K] = min(dp[i][K], dp[j - 1][K - 1] + self.count(s[j - 1:i]))

        return dp[m][k]

    def count(self, string):
        left = 0
        right = len(string) - 1
        count = 0
        while left < right:
            if string[left] != string[right]:
                count += 1
            left += 1
            right -= 1
        return count