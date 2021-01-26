class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        self.memo = {}
        return self.dfs(0, len(arr) - 1, arr)

    def dfs(self, i, j, arr):
        if i > j:
            return 0
        if i == j:
            return 1
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        # 第一种情况， 如果 i 到 j 中 没有任何一个数跟j相等的， 那么直接把j 移除
        result = self.dfs(i, j - 1, arr) + 1
        # 第二种情况， k 如果 和 j 相邻， 也需要1 cost 移除
        if arr[j] == arr[j - 1]:
            result = min(result, self.dfs(i, j - 2, arr) + 1)
        # 第三种情况，从i到j中， 寻找一个与j相等的k， 来一起移除掉，这样cost 就是 0
        for k in range(i, j - 1):
            if arr[k] == arr[j]:
                result = min(result, self.dfs(i, k - 1, arr) + self.dfs(k + 1, j - 1, arr))

        self.memo[(i, j)] = result
        return result