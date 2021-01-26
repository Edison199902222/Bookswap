'''
graph 建立图
然后 把 对应的机场排序
从起点出发， 一直走， 边走边把边给去掉
当没有边可以走的时候，说明我们到了终点
把终点放进result

'''


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = {}
        # building graph
        for start, end in tickets:
            if start not in graph:
                graph[start] = []
            graph[start].append(end)
        # 排好序，这样输出的时候才可以按照字母顺序输出，我们需要先去字母小
        for keys in graph.keys():
            graph[keys].sort(reverse=True)

        result = []
        stack = ["JFK"]
        while stack:
            cur = stack[-1]
            if cur in graph and len(graph[cur]) > 0:
                stack.append(graph[cur].pop())  # 把要去的机场pop出来， 放进stack中, 也相等于 删除边， 这样不会重复访问
            else:
                result.append(stack.pop())  # 当没有机场可以去的时候， 说明我们到终点了。那么把stack最后一个加入进result中
        return result[::-1]  # 因为是dfs 我们从起点出发到终点，再把终点先放进resul中的


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 欧拉回路
        graph = collections.defaultdict(list)
        for start, end in tickets:
            graph[start].append(end)
        # 排好序，这样输出的时候才可以按照字母顺序输出，我们需要先去字母小的
        for node in graph:
            graph[node] = sorted(graph[node], reverse=True)
        self.result = []
        self.dfs(graph, "JFK")
        # 最后result 需要逆序，因为 先走字母小的， 也就是到终点开始才添加，终点是第一个点
        return self.result[::-1]

    def dfs(self, graph, cur):
        # 尝试去走每个路径
        for i in range(len(graph[cur])):
            if graph[cur]:
                # 走的同时pop
                new = graph[cur].pop()
                self.dfs(graph, new)
        # 只有没有路可以走的时候，我们才开始添加result
        self.result.append(cur)
        return





