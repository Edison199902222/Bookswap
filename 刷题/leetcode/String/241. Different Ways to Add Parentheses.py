'''
用递归的方式
先遍历字符串
遇到operator 就拆成两部分递归
然后求出左部分 跟右部分
合并在一起 因为左部分 和右边部分 其实都是list 里面含有很多个数字
然后遍历两个list 相加才是最终结果
'''


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        self.memo = {}
        return self.dfs(input)

    # 问题本质是，不用假设括号，而是只要遇到计算符号，我们就可以分成左边右边，然后分情况计算结果
    # 并且不能只用index 去， 因为相同index 的情况下 result 是不一样的，只有string 相同的情况下，result 才是固定的！！
    # result 是 对应string下 所有可能的结果 再对左右进行组合
    def dfs(self, s):
        if s.isdigit():
            return [int(s)]
        if s in self.memo:
            return self.memo[s]
        result = []
        for i in range(len(s)):
            # 把左右部分拆分开来计算
            if s[i] in "*-+":
                left = self.dfs(s[:i])
                right = self.dfs(s[i + 1:])
                for x in left:
                    for y in right:
                        result.append(self.helper(x, y, s[i]))
        self.memo[s] = result
        return result

    def helper(self, x, y, operation):
        if operation == "+":
            return x + y
        if operation == "-":
            return x - y
        if operation == "*":
            return x * y
if __name__ == "__main__":
    solution = Solution()
    print(solution.diffWaysToCompute("2-1-1"))
