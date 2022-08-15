'''
dfs + 回溯法
遍历字符串
先从 长度为1 的回文字母开始
每个 单独的字母 都作为一个dfs的开始 一直往深里走
比如 abb
先 把a 添加到temp里 然后剩下的字母 bb 作为s 继续dfs
然后 又长度为 1 开始 b 和 b returen 之后 bb作为长度为2的 判断是不是回文
总体思路就是 往深里搜索 


'''


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        self.dfs(s, [])
        return self.result

    def dfs(self, s, path):
        if not s:
            self.result.append(path[:])
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if self.decide(prefix):
                path.append(prefix)
                self.dfs(s[i:], path)
                path.pop()

    def decide(self, s):
        return s == s[::-1]
if __name__ == "__main__":
    solution = Solution()
    print(solution.partition("abb"))
