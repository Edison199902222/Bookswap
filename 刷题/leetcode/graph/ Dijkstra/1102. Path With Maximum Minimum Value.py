class Solution(object):
    def maximumMinimumPath(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        heap = []
        heapq.heappush(heap, (-A[0][0], 0, 0))
        seen = set()
        seen.add((0, 0))
        while heap:
            value, i, j = heapq.heappop(heap)
            if i == len(A) - 1 and j == len(A[0]) - 1:
                return -value
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if (x, y) in seen or x < 0 or y < 0 or x >= len(A) or y >= len(A[0]):
                    continue
                seen.add((x, y))
                heapq.heappush(heap, (max(value, -A[x][y]), x, y))
        return -1
'''
一开始用dp 写错了
这道题具有后效性，也就是当前点i，j 并不一定只跟四个方向有关，跟前面的也有关系
阶段与阶段之间没有什么必然的顺序
https://baike.baidu.com/item/%E6%97%A0%E5%90%8E%E6%95%88%E6%80%A7
'''