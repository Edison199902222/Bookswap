'''
设置初始值
dp[0]时 为true
dp[i]表示 到第i个长度为止的string 是不是可以被word dic 表示出来
从string的第二个 遍历
并且j 从头到 i 遍历
如果一个 i 长度的string
如果它的substring j 是true的话 同时 它的 另外一部分j 到 i 又在word dic中
说明整个就是true
'''

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if s is None or wordDict is None:
            return False
        length = len(s)
        dp = [False for i in range(length+1)]
        dp[0] = True
        for i in range(1,length+1):
            for j in range(0,i):
                substring = s[j:i]
                if dp[j] and substring in wordDict:
                    dp[i] = True
                    break
        return dp[length]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.memo = {}
        wordDict = set(wordDict)
        return self.dfs(s, len(s), wordDict)

    # dp[i] 表示 前 i 个 元素 是不是可以用worddict表示出来
    def dfs(self, s, index, wordDict):
        if index == 0:
            return True
        if index in self.memo:
            return self.memo[index]

        result = False
        for i in range(index):
            # 枚举start， 如果 start 到 index 这一段在 worddict中的话，那么我们只需要检查前start个 元素是不是可以被worddict表示
            temp = s[i: index]
            if temp in wordDict and self.dfs(s, i, wordDict):
                result = True
                break

        self.memo[index] = result
        return result

if __name__ == "__main__":
    solution = Solution()
    s = "leetcode"
    h = ["leet","code"]
    print(solution.wordBreak(s,h))