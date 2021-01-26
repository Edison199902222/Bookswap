class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.dfs(n, k, [], 0)
        return self.result

    def dfs(self, n, k, path, prev):
        if len(path) == k:
            self.result.append(path[:]) # copy
            return
        for i in range(prev + 1, n + 1):
            if i in path:
                continue
            path.append(i)
            self.dfs(n, k, path, i)
            path.pop()


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.dfs(n, k, 1, [])
        return self.result

    def dfs(self, n, k, index, path):
        if len(path) == k:
            self.result.append(path[:])

        for i in range(index, n + 1):
            path.append(i)
            self.dfs(n, k, i + 1, path)
            path.pop()


'''
去重方法上 每次记录前一个的值
每次递归下去 值取 比前一个值大的地方
而且 记住 如果遇到回溯需要pop元素的话 那么我们需要 【：】 deep copy
'''
if __name__ == "__main__":
    solution = Solution()
    print(solution.combine(4,2))