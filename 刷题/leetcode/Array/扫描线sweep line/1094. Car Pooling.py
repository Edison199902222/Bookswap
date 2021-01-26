class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if not trips or not trips[0]:
            return True
        heap = []
        for number, dis1,dis2 in trips:
            heapq.heappush(heap, (dis1, number))
            heapq.heappush(heap, (dis2, -number))
        cur_pass = 0
        while heap:
            dis, number = heapq.heappop(heap)
            cur_pass += number
            if cur_pass > capacity:
                return False
        return True