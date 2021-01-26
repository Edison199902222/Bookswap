class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: int
        """
        self.memo = {}
        return self.dfs(0, 0, workers, bikes)

    def helper(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # dp (index, visited) 表示当前给第index个worker 分配时 自行车visited分配情况 的最小sum
    def dfs(self, index, visited, workers, bikes):
        if index == len(workers):
            return 0
        if (index, visited) in self.memo:
            return self.memo[(index, visited)]

        result = float("inf")
        for i, bike in enumerate(bikes):
            # visited 是一个二进制 代表现在 自行车分配的情况，比如 0001， 代表 现在一号车被分配了， 1 代表分配了， 0 代表还没有被分配
            # 1 << i 代表如果当前第i 辆车被分配后， 跟之前分配的情况 去交集
            # 比如 visited 0001 代表当前第一辆车被分配了， 如果1 << i = 0001， 那么 & 后，还是等于0001
            # 这代表两个set 有交集，说明有一辆车被分配了两次
            if visited & 1 << i:
                continue
            # visited | 1 << j, 两个为0 则为0，一个个为1 则为1， 意思是取并集合， 比如 0001， 0010， 会变成0011， 意思就代表第一辆车跟第二辆车都被分配了
            result = min(result,
                         self.helper(workers[index], bike) + self.dfs(index + 1, visited | 1 << i, workers, bikes))

        self.memo[(index, visited)] = result
        return result
