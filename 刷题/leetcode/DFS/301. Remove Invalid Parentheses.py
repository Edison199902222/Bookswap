'''
isvalid 用来检查还有几个括号需要移动
dfs 每次把现在的括号去掉
然后 并且检查 这个new string 之前没有访问过 因为如果访问过 会导致重复的情况 并且需要小于n
利用评价函数计算字符串中未匹配括号的个数

尝试从输入字符串中移除括号，若得到的新字符串的失配括号比原字符串少，则继续搜索；

否则剪枝。
'''

class Solution(object):
    def removeInvalidParentheses(self, s):
        res = []
        self.visited = set([s])
        self.dfs(s, self.invalid(s), res)
        return res

    def dfs(self, s, n, res):
        if n == 0:
            res.append(s)
            return
        for i in range(len(s)):
            if s[i] in ('(', ')'):
                new_s = s[:i] + s[i + 1:]
                if new_s not in self.visited and self.invalid(new_s) < n:
                    self.visited.add(new_s)
                    self.dfs(new_s, self.invalid(new_s), res)

    def invalid(self, s):
        plus = minus = 0
        memo = {"(": 1, ")": -1}
        for c in s:
            plus += memo.get(c, 0)
            minus += 1 if plus < 0 else 0
            plus = max(0, plus)
        return plus + minus
if __name__ == "__main__":
    solution= Solution()
    print(solution.removeInvalidParentheses("()())()"))