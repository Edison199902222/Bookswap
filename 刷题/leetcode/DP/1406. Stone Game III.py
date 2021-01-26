class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        self.memo = {}
        # 每次跟对手的得分 相减，如果result 大于0，则alice 胜，小于0 bob 胜， 等于0就是平局
        result = self.dfs(0, stoneValue)
        if result == 0:
            return "Tie"
        elif result < 0:
            return "Bob"
        else:
            return "Alice"

    def dfs(self, index, stone):
        if index >= len(stone):
            return 0
        if index == len(stone) - 1:
            return stone[index]
        if index in self.memo:
            return self.memo[index]
        result = stone[index] - self.dfs(index + 1, stone)
        if index + 1 < len(stone):
            result = max(result, stone[index] + stone[index + 1] - self.dfs(index + 2, stone))
        if index + 2 < len(stone):
            result = max(result, stone[index] + stone[index + 1] + stone[index + 2] - self.dfs(index + 3, stone))
        self.memo[index] = result
        return result
