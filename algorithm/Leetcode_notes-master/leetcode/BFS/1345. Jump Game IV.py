class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # 看到最短路径，需要想到bfs 或者dp
        # 因为数据量，所以只能用bfs on 解法
        # 创建一个相同node val 可以跳跃的图
        graph = collections.defaultdict(list)
        for i in range(len(arr)):
            graph[arr[i]].append(i)

        start_node = 0
        target = len(arr) - 1
        queue = collections.deque()
        queue.append((start_node, 0))
        visited = set()
        visited.add(start_node)
        # 每次走一个node，看看能走到哪
        while queue:
            node, step = queue.popleft()
            if node == target:
                return step
            for i in graph[arr[node]][::-1]:
                if i not in visited:
                    visited.add(i)
                    queue.append((i, step + 1))
                    # 要把走过的node pop出来，降低时间复杂度，这样下次如果遇见了，就不会再循环一遍
                    graph[arr[node]].pop()

            for i in [node - 1, node + 1]:
                if 0 <= i < len(arr) and i not in visited:
                    visited.add(i)
                    queue.append((i, step + 1))
        return -1
