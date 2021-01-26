'''
用heap做 更快
先把整个数组排序
然后使用heap 保存k个 最大的数
heap是最小堆 最上面的就是第k个大的数

'''
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        self.heap = nums[-k:]
        self.k = k
        heapq.heapify(self.heap)
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap,val)
        elif val >= self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]
