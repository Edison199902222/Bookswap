class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        temp = sorted(costs, key=lambda x: x[0] - x[1])
        result = 0
        for i in range(len(temp) // 2):
            result += temp[i][0]
        for i in range(len(temp) // 2, len(temp)):
            result += temp[i][1]
        return result
'''
greedy 
先排序 用lambda 函数 把 costs a - costs b 的差 来进行排序
这样的意义是 把所有A 比 B  的差 小的 放在前面 意思是 去a 比 去b 花的更少
然后这一半的人 去A
后一半就去 b
'''


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        self.memo = {}
        N = len(costs) // 2
        return self.dfs(N, N, costs, N)

    def dfs(self, n1, n2, costs, N):
        if n1 + n2 == 0:
            return 0
        if (n1, n2) in self.memo:
            return self.memo[(n1, n2)]
        result = float("inf")
        if n1 > 0:
            result = min(result, costs[n1 + n2 - 1][0] + self.dfs(n1 - 1, n2, costs, N))
        if n2 > 0:
            result = min(result, costs[n1 + n2 - 1][1] + self.dfs(n1, n2 - 1, costs, N))
        self.memo[(n1, n2)] = result
        return result

'''
(n1,n2)表示 当前 分配到城市A 有n1 个人 分配到城市B 有 n2个人 所组成的最小花费
'''