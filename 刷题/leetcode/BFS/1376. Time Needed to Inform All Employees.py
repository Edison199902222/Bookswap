class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        # 因为每一条路径上的node都是单独和父亲节点算时间的，所以想到bfs 的时候，要把当前时间和node 作为key 放进去
        graph = collections.defaultdict(list)
        for index, value in enumerate(manager):
            if index == headID:
                continue
            graph[value].append(index)
        result = 0
        node = headID
        queue = collections.deque()
        queue.append((node, 0))
        while queue:
            cur, time = queue.popleft()
            result = max(result, time)
            for neighbor in graph[cur]:
                queue.append((neighbor, time + informTime[cur]))
        return result

