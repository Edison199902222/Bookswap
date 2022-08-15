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
Time: O(MN log MN), since for each element in matrix we have to do a heap push, which cost O(log # of element in the heap) times. The size of the heap can grow up to # of elemnts in the matrix.
Space: O(MN). We need to keep track of the elements we have seen so far. Finally the size of seen will grow up to # of items in the matrix
'''