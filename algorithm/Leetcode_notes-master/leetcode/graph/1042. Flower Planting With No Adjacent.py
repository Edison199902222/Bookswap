class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        graph = {x:[] for x in range(N)}
        result = [0] * N
        # building graph
        for start, end in paths:
            graph[start - 1].append(end - 1)
            graph[end - 1].append(start - 1)
        # 尝试从第一个花园开始插颜色
        for i in range(N):
            neighbour_color = []
            # 找出邻居颜色
            for neighbour in graph[i]:
                neighbour_color.append(result[neighbour])
            for color in range(1, 5):
                if color in neighbour_color:
                    continue
                result[i] = color
                break
        return result
'''
总体思路：由于每个顶点最多只有三条边，所以时间复杂度是O(N)
创建图， 创建图以后
我们对于每一个花园 找出它所有邻居的花的颜色
然后我们在1 到 4 的花中寻找 一个跟邻居不同的花的颜色分配给当前花园
'''