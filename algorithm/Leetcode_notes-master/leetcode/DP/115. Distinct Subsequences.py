'''
dp
比较两个字符串一般都用dp
如果字符串当前相等 那么数量就会等于 去掉这个字符串之前的 + 跳过这个字符串的
dp[i][j] = dp[i-1][j-1] + dp[i][j-1] i表示t中的字符串 j表示s中的字符串
'''

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = [[0 for i in range(len(s)+1)] for i in range(len(t)+1)]
        for i in range(len(s)+1):
            dp[0][i] = 1
        for i in range(1,len(t)+1):
            for j in range(1,len(s)+1):
                if s[j-1] == t[i-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]
if __name__ == "__main__":
    solution = Solution()
    a = "rabbbit"
    b =  "rabbit"
    print(solution.numDistinct(a,b))