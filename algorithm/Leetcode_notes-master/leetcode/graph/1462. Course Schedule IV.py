class Solution(object):
    def checkIfPrerequisite(self, n, prerequisites, queries):
        """
        :type n: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        graph = collections.defaultdict(set)
        check = set()
        # 建立图
        for u, v in prerequisites:
            graph[u].add(v)
            check.add((u, v))
        result = []
        # 对每个query来说
        for a, b in queries:
            # 如果在check
            if (a, b) in check:
                result.append(True)
                continue
            if (b, a) in check:
                result.append(False)
                continue
            # 创建deque
            queue = collections.deque()
            visited = set()
            queue.append(a)
            flag = False
            # 把a作为起点，遍历一遍图，如果可以走到，那么就append true，不可以的话 append false
            while queue:
                node = queue.popleft()
                if node == b:
                    flag = True
                    continue
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor)
            result.append(flag)
        return result

