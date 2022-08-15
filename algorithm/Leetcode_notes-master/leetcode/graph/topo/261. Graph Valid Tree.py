import collections


class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n - 1:
            return False
        dic = collections.defaultdict(set)
        for i, j in edges:
            dic[i].add(j)
            dic[j].add(i)
        stack = [0]
        visited = set()
        while stack:
            node = stack.pop()
            if node in visited:
                return False
            visited.add(node)
            for i in dic[node]:
                stack.append(i)
                dic[i].remove(node)
            dic.pop(node)
        return not dic

'''
要判断一个图是不是tree 有两个条件
第一个条件 所有的node 都是联通的 也就是 所有的node我们都要访问
第二个条件 没有环
所以 我们创建一个字典 把所有node 与它的邻居 对应上
创建 visit的一个set 来判断node有没有被第二次访问
然后 用stack 进行dfs
从第0 号node 开始 我们先判断当前node 是不是在visit中 
如果在的话 说明被第二次访问了 那么就说明有环 直接return false
然后把node 添加进 visit中 
遍历 邻居节点 把邻居节点放进stack的同时 还要删除邻居节点到node 的边 
因为 有向图 与 无向图的区别就是 A B 两个点 有向图只会创建一条边 A -> B 但是无向图 会创建两个边 A ->B, B -> A
只要同时删除邻居节点到node的边的话 只要没有环 这样就可以保证一个node只被访问一次
遍历完邻居节点后 我们把node在字典中删除掉
这样遍历完所有的node之后 就可以检查是不是 所有的node我们都访问了
'''


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return False
        if len(edges) != n - 1:
            return False
        graph = {x: [] for x in range(n)}
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        queue = collections.deque([0])
        visited = set()
        while queue:
            node = queue.popleft()
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour in visited:
                    continue
                queue.append(neighbour)
        return len(visited) == n
'''
用bfs 的版本， 跟dfs不一样的是， dfs 每次会把边移除 
把所有 能访问到的node 全部放进visited中
如果 一个图中有环的话，那么肯定这里面的节点 不能都被访问一遍
所以最后只需要判断 visited中 是不是有所有的节点
'''


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False
        # 拓扑排序 每次移除入度为1的node， 如果是tree的话，那么走完的node 必然 是node 的总数
        graph = collections.defaultdict(list)
        in_degree = {node: 0 for node in range(n)}
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
            in_degree[end] += 1
            in_degree[start] += 1
        # 找 入度小于等于1 的作为起点
        start_node = [node for node in in_degree if in_degree[node] <= 1]
        queue = collections.deque(start_node)
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            print(node, "111")
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                print(neighbor, in_degree[neighbor])
                # 因为起点把所有入度为0都走过了，所以之后只走入度为1的， 入读为1 等于 direct graph 中的入读为0 因为是双向的
                # 使用queue 来做拓扑排序 保证了入度为0/1 的优先走 并且不会走回头路
                if in_degree[neighbor] == 1:
                    queue.append(neighbor)

        return True if count == n else False
