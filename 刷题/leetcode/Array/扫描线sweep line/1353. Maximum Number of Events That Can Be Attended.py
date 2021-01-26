class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        # 思路：对于当前天来说，我们希望参加 的是 当前以及开始的会议， 如果有多个开始的会议，那么我们会选择结束时间较早的
        # 因为时间结束时间越晚的，可以选择的天数就更多 贪心的思想
        # 先按照开始时间跟结束时间排序 并且倒叙，为了方便pop， 用heap 动态维护当前可以选择参加的会议
        events.sort(reverse=True, key=lambda x: (x[0], x[1]))
        result = 0
        heap = []
        for i in range(1, 10 ** 5 + 1):
            # 把当天 无效的会议pop掉，heap中只存结束时间
            while heap and heap[0] < i:
                heapq.heappop(heap)
            # 把当前天 开始进行的会议也放进来
            while events and events[-1][0] <= i:
                heapq.heappush(heap, events.pop()[1])
            if heap:
                result += 1
                heapq.heappop(heap)
            if not heap and not events:
                break
        return result


