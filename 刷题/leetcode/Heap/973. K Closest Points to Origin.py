class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        heap = []
        result = []
        for x, y in points:
            distance = -(x * x + y * y)
            if len(heap) == K:
                heapq.heappushpop(heap, (distance, x, y))
            else:
                heapq.heappush(heap, (distance, x, y))

        for _, x, y in heap:
            result.append([x, y])
        return result
'''
这道题其实就是 算出distance之后
求 距离最小的前k个元素
因为heap中 只有最小堆
所以我们采用取反，把heap变成最大堆
每一次 我们push distance 跟坐标 进去
然后当 heap的长度 等于我们k之后， 我们把最大值pop出去，这样我们就保证了heap中是前k个最小的元素
'''