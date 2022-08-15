import functools


class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        self.memo = {}
        return self.dfs(0, 0, rods)

    # dp[i][s] 意思是 前i个元素，左右高度差为s的 largest possible height of your billboard installation.
    def dfs(self, i, s, rods):
        # 走到最后发现s不等于0的话，说明这条路不对， 设置为最小数
        # s 代表 左边set 跟右边set的差
        if i == len(rods):
            return 0 if s == 0 else float("-inf")
        if (i, s) in self.memo:
            return self.memo[(i, s)]
        # 三种情况， 第一种 不把当前的元素放在任何一个set中
        # 第二种情况，把当前元素放进左边，所以 s变大, 并且加上rods[i]
        # 第三种情况，把当前元素放进右边，所以s 变小
        # 取最大值，
        result = max(self.dfs(i + 1, s, rods), self.dfs(i + 1, s + rods[i], rods) + rods[i],
                     self.dfs(i + 1, s - rods[i], rods))
        self.memo[(i, s)] = result
        return result



class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        @functools.lru_cache(None)
        def dfs(i, s):
            if i == len(rods):
                return 0 if s == 0 else float("-inf")
            result = max(dfs(i + 1, s), dfs(i + 1, s + rods[i]) + rods[i], dfs(i + 1, s - rods[i]))
            return result
        return dfs(0,0)