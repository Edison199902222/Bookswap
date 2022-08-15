class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        heap = [1]
        visited = set()
        visited.add(1)
        value = None
        while n > 0:
            value = heapq.heappop(heap)
            n -= 1
            for factor in primes:
                temp = factor * value
                if temp in visited:
                    continue
                visited.add(temp)
                heapq.heappush(heap, temp)
        return value
'''
与264 一样的思路
'''