import heapq
def profit(num, inventor, order):
    heap = [-i for i in inventor]
    heapq.heapify(heap)
    result = 0
    while heap:
        current_sell = heapq.heappushpop(heap)
        result += current_sell