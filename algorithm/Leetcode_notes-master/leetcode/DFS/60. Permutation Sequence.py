class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        self.count = 0
        self.result = []
        self.dfs(n, [], k, [])
        result = ""
        for i in self.result[0]:
            result += str(i)
        return result
    def dfs(self, n, path, k, visited):
        if len(path) == n:
            self.count += 1
            if self.count == k:
                self.result.append(path[::])
            return
        for i in range(1, n + 1):
            if i in visited:
                continue
            path.append(i)
            visited.append(i)
            self.dfs(n, path, k, visited)
            path.pop()
            visited.pop()


if __name__ == "__main__":
    solution = Solution()
    print(solution.getPermutation(3,3))