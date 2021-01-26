"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        heap = []
        # 把每个雇员 的第一个开始时间放进去， 并且记录雇员number 和 第几个working time
        for number, employee in enumerate(schedule):
            heap.append((employee[0].start, number, 0))
        heapq.heapify(heap)
        result = []
        # 记录下前一个 end， 初始化设置为start 是因为第一个没有空闲时间
        prev_end = heap[0][0]
        while heap:
            cur_start, number, time_index = heapq.heappop(heap)
            # 看当前start 是不是大于前面的end
            if cur_start > prev_end:
                result.append(Interval(prev_end, cur_start))
            # 更新当前end
            prev_end = max(prev_end, schedule[number][time_index].end)
            # 如果当前雇员 还有 下一个 工作时间的话
            if time_index + 1 < len(schedule[number]):
                heapq.heappush(heap, (schedule[number][time_index + 1].start, number, time_index + 1))
        return result

