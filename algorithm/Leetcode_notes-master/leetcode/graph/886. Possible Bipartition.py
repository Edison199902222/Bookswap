class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        if not N:
            return False
        graph = collections.defaultdict(list)
        # 建立每个人 跟他与之对应不喜欢的人的表
        for node1, node2 in dislikes:
            graph[node1 - 1].append(node2 - 1)
            graph[node2 - 1].append(node1 - 1)
        # 尝试分配颜色， 未分配的人的颜色是0
        color = [0 for i in range(N)]
        for node in range(N):
            # 如果颜色是0， 并且有不喜欢的人的话， 我们尝试去染色
            if color[node] == 0 and len(graph[node]) > 0:
                # 尝试分配1 的颜色
                color[node] = 1
                if not self.dfs(graph, color, node):
                    return False
        return True

    def dfs(self, graph, color, current):
        # 遍历不喜欢的人列表
        for neighbor in graph[current]:
            # 还未染色的话， 给不喜欢的人染成跟自己相反的颜色， 然后dfs下去
            if color[neighbor] == 0:
                color[neighbor] = -color[current]
                if not self.dfs(graph, color, neighbor):
                    return False
            # 如果染了颜色的话， 检查跟自己的颜色是不是相同的， 如果是相同的话 return false
            elif color[neighbor] == color[current]:
                return False
        return True


'''
整体思路就是 
建立每个人 和他对应的 不喜欢的人的列表
尝试给每一个人分配颜色1， 并且 如果他有不喜欢的人的话， 尝试把不喜欢的人 染成跟自己相反的颜色，然后dfs 下去
如果 发现 不喜欢的人的颜色 跟 自己颜色相同， 直接return False
'''