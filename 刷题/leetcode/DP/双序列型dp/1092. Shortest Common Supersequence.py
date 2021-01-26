class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        m = len(str1)
        n = len(str2)
        dp = [[float("inf")] * (n + 1) for i in range(m + 1)]
        # 初始化
        for i in range(m + 1):
            dp[i][0] = i

        for i in range(n + 1):
            dp[0][i] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 相等的话，i 跟 j只需要加上其中一个就可以涵盖所有了
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                # 不相等的话，选取其中一个 加入 scs， 涵盖所有
                # 如果i - 1， j小的话，把i 加入scs 涵盖所有字母
                # 如果i， j - 1 小的话， 把j 加入scs 涵盖所有字母
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1)
        # 重构 scs，就是把dp 从 m， n 还原到 base case的情况
        i = m
        j = n
        result = []
        while i > 0 or j > 0:
            # 如果i j 都大于等于0，意思是如果可以比较的话
            # 如果dp[i][j]是由dp[i-1][j-1]+1得来,也即是说str1[i]==str2[j]
            # 那么就意味着当时在构建SCS的时候，最后一步是在dp[i-1][j-1]的基础上加上i
            if i - 1 >= 0 and j - 1 >= 0 and str1[i - 1] == str2[j - 1]:
                result.append(str1[i - 1])
                i -= 1
                j -= 1
            else:
                # 如果dp[i][j]是由dp[i-1][j]+1得来,那么说明当时是在dp[i-1][j]的基础上加上str1[i]，
                # 现在逆序重构的时候需要先加上str1[i].
                if dp[i - 1][j] < dp[i][j - 1]:
                    result.append(str1[i - 1])
                    i -= 1

                else:
                    # 如果dp[i][j]是由dp[i][j-1]+1得来,那么说明当时是在dp[i][j-1]的基础上加上str2[j]
                    # 现在逆序重构的时候需要先加上str2[j].
                    result.append(str2[j - 1])
                    j -= 1
        return "".join(result[::-1])