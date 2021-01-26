class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        heap = [1]
        visited = set()
        visited.add(1)
        value = None
        for i in range(n):
            value = heapq.heappop(heap)
            for factor in [2,3,5]:
                if value * factor not in visited:
                    visited.add(value * factor)
                    heapq.heappush(heap, value * factor)
        return value
'''
使用heap 维护住始终用最小的ugly number
 visited set 维护住 没有重复的ugly number
一般是 我们check 每一个 数 是不是ugly number 但是 这样复杂度太高了
我们就用1 乘 factor 2 3 5 这样 得出来的每一个数就肯定是ugly number
并且 我们把乘出来的数字 放进min heap中 
下一次 我们把 min heap 拿出一个元素， 这个元素是在现有ugly number中最小的那个
我们再用它乘 factor 2 3 5 又会得到新的 ugly number 放进heap中
这样每一次 我们都拿出最小的ugly number  直到第n 次
'''