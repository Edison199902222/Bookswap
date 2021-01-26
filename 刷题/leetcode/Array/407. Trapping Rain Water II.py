class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        heap = []
        result = 0
        visited = [[0] * len(heightMap[0]) for i in range(len(heightMap))]
        for i in range(len(heightMap)):
            for j in range(len(heightMap[0])):
                if i == 0 or i == len(heightMap) - 1 or j == 0 or j == len(heightMap[0]) - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = 1
        while heap:
            height, i, j = heapq.heappop(heap)
            for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                new_x = i + x
                new_y = j + y
                if 0 <= new_x < len(heightMap) and 0 <= new_y < len(heightMap[0]) and visited[new_x][new_y] != 1:
                    result += max(0, height - heightMap[new_x][new_y])
                    heapq.heappush(heap, (max(height, heightMap[new_x][new_y]), new_x, new_y))
                    visited[new_x][new_y] = 1
        return result
'''
这是上一道题的一个follow up
在2d 中
visited 来代表 某个点遍历过没有
我们可以先把边界所有的值 放进heap中 并且设置 visited 
然后我们在边界中的最小值开始 往里面比较 因为最小值决定了 这个灌水能灌多深
最小值开始 上下左右搜索， 如果当前的值 比我们最小值要小 那么我们就开始灌水 灌到最小值这个高度
如果比我们大 我们就不灌水
灌水结束后 我们把当前最高的柱子（ 是之前那个边界高 还是当前柱子高） 放进heap中
并且把visit 设置为 已经遍历过

'''