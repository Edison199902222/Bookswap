class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon or not dungeon[0]:
            return
        self.memo = {}
        # returns minimum possible amount of health required at position (i, j)
        m = len(dungeon)
        n = len(dungeon[0])
        return self.dfs(0, 0, m, n, dungeon)
        print(self.memo)

    def dfs(self, i, j, m, n, dungeon):
        if i >= m or j >= n:
            return float("inf")

        if (i, j) in self.memo:
            return self.memo[(i, j)]
        if i == m - 1 and j == n - 1:
            # 每一个格子至少需要1的血量，负数的话 那么至少需要 变正数 + 1的血量
            # 正数的话，变负数 + 1， 跟 1 取最大值就行， 正数只需要1
            return max(1, - dungeon[i][j] + 1)
        # 取最小的血量， 之前格子返回的 跟 1 取最大 因为会有负数， 负数代表只需要最低血量1
        left = self.dfs(i + 1, j, m, n, dungeon)

        up = self.dfs(i, j + 1, m, n, dungeon)

        cur_cost = min(max(1, left - dungeon[i][j]), max(1, up - dungeon[i][j]))

        self.memo[(i, j)] = cur_cost
        return cur_cost


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        # 对于当前格子，至少需要多少血量才能走到终点
        @functools.lru_cache(None)
        def dfs(i, j):
            if i >= m or j >= n:
                return float("inf")
            # 对于最后一个格子来说，至少需要多少的生命才能不死
            if i == m - 1 and j == n - 1:
                return max(1, - dungeon[i][j] + 1)

            right = dfs(i, j + 1)
            down = dfs(i + 1, j)
            # 对于当前格子最少需要的血量，取决于右边 跟 下面 格子至少多少的血量
            # 用右边/下面 格子 要求的血量， 减去当前格子的血， 就能知道 至少需要多少血量可以从当前格子 走到下一个格子
            result = min(max(1, right - dungeon[i][j]), max(1, down - dungeon[i][j]))
            return result

        m = len(dungeon)
        n = len(dungeon[0])
        return dfs(0, 0)


'''
注意dp题 如果是坐标类的话
注意方向 这题如果return m - 1， n -1 是不行的， 因为m - 1， n - 1 时是把终点当成起点， 终点和起点的血量是不一样的
'''