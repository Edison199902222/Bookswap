
'''
想法： 其实我们 维持两个 heap
左边是max  右边是min
左边 max heap 意思是 维持一个 由数组中 最小几个数组成的heap
右边 min heap 意思是 维持一个 由数组中 最大几个数组成的heap
如果 两个长度相等时
那么mediam  其实就是 两个heap 的顶部 和 除 2

维持 max == min  或者 max+1 = min

每次有一个数字进来
我们先把他放进min里面 min中就是整个数组中最大的数
再pop最小值
取反 放入数组中最小数组 max中 取反的目的就是 越小的数字在下面 越大的数字在顶部
因为我们需要max 中的最大的数字 也就是栈顶 所以我们需要越大的数字在上面 所以取反
检查如果max 大于min 的话 再把max里面的最大值pop出来 放进min里面
find median 的话 就是 如果两边相等
就是 顶端相加 除2
如果不想等的话 因为min 比max多一个 所以把min的顶端pop
'''


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = []
        self.max = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # 先放进右边再拿出来最小的那个
        # 再放进左边， 这样保证了order 是升序的
        heapq.heappush(self.max, -heapq.heappushpop(self.min, num))
        # 放完后，检查左边的是不是只比右边 大一个 或者相等
        if len(self.max) - 1 > len(self.min):
            heapq.heappush(self.min, - heapq.heappop(self.max))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.min) == len(self.max):
            return (self.min[0] - self.max[0]) / 2
        else:
            return -self.max[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap1 = []
        self.heap2 = []

    def addNum(self, num: int) -> None:
        if not self.heap1:
            heapq.heappush(self.heap1, -num)
            return
        if not self.heap2:
            heapq.heappush(self.heap2, -heapq.heappushpop(self.heap1, -num))
            return
        if num <= -self.heap1[0]:
            heapq.heappush(self.heap1, - num)
            if len(self.heap1) - 1 > len(self.heap2):
                heapq.heappush(self.heap2, -heapq.heappop(self.heap1))
        else:
            heapq.heappush(self.heap2, num)
            if len(self.heap2) > len(self.heap1):
                heapq.heappush(self.heap1, -heapq.heappop(self.heap2))

    def findMedian(self) -> float:
        if len(self.heap1) == len(self.heap2):
            temp = -self.heap1[0] + self.heap2[0]
            return temp / 2
        else:
            return - self.heap1[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()