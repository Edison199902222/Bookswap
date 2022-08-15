import collections


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = collections.defaultdict(set)
        for (x, y), v in zip(equations, values):  # 意思是 把两个东西的第一个元素 和 另一个东西的第一个元素组合
            graph[x].add((y, v))
            graph[y].add((x, 1.0 / v))
        result = []
        for var1, var2 in queries:
            temp = self.dfs(graph, var1, var2, set())
            result.append(temp)
        return result

    def dfs(self, graph, start, end, visited):
        if start == end and start in graph:
            return 1.0
        visited.add(start)  # 如果没有visited 会出现节点反复访问， 因为是双向图！！！ 比如 a去b， b又去a
        for neighbor, in_degre in graph[start]:
            if neighbor in visited:
                continue
            temp = self.dfs(graph, neighbor, end, visited)
            if temp > 0:
                return in_degre * temp  # in_degree = a/b temp = b/c 要 a/c = a/b * b/c

        return -1.0


'''
zip 意思是 把两个东西的第一个元素 和 另一个东西的第一个元素组合 
a = [1,2,3]
 b = [4,5,6]   zipped = zip(a,b)  等于 (1, 4), (2, 5), (3, 6)]
可以把问题转化成图的问题
已知a/b b/c 怎么求 a/c
数学上来说 只需要 a/c * b/c就可以了
我们把这个转化成图的问题， a node  到 c node  edge 是 a/c 的值 反过来 c 到 a edge 是 1/(a/c）的值

那么 我们建立一个字典 key 是 初始的node value 是一个set 由 终点node 跟 edge 组成
然后我们遍历 queries， 把起点和终点放进dfs中 递归进行处理， 返回的值是最后的结果

dfs 函数中
base case 是start == end 的话，并且start 在我们graph 中存在的话 我们直接return 1
先把当前start node 放进visited中 避免反复访问
然后 遍历他的邻居节点， 把邻居节点作为start 继续dfs 这样就可以求出 邻居节点到end的值 也就是邻居节点/ end 的值
最后 如果邻居节点 到end 的值 是大于0的，因为小于0 表示 我们找不到边
大于0 的话 我们就return 当前的值 * 邻居节点到end 的值 
如果都不满足 我们直接return -1 就行
'''
