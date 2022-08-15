class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        # 树/图的dfs 还可以return counter
        # 像后序遍历，先统计 左 右子树 所有字母有几个的情况，然后return 到当前层
        # 再处理 当前层的字母， 把当前层的字母 + 1
        # 然后再把当前层字母的数量，加到result之中
        self.result = [0] * n
        graph = collections.defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        self.dfs(0, None, graph, labels)
        return self.result

    def dfs(self, cur_node, parent, graph, labels):
        # 每一层都建立一个counter 统计 当前层 以及所有子树的字母
        counter = collections.Counter()
        for child in graph[cur_node]:
            if child == parent:
                continue
            counter += self.dfs(child, cur_node, graph, labels)
        counter[labels[cur_node]] += 1
        self.result[cur_node] += counter[labels[cur_node]]
        return counter