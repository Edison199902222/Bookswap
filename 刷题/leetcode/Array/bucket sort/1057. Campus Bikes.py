class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        #最远的曼哈顿距离是， 一个在0，0， 一个在1000， 1000， 是2000
        # 曼哈顿距离所有可能性不会超过2000， 所以可以用bucket
        bucket = [[] for i in range(2001)]
        # index 越小的worker 会 越放在桶子的前面
        # 后面分配时，距离如果一样，index 小的work会分配
        for i, (w_x, w_y) in enumerate(workers):
            for j, (b_x, b_y) in enumerate(bikes):
                distance = abs(w_x - b_x) + abs(w_y - b_y)
                bucket[distance].append((i, j))
        result = [-1] * len(workers)
        # 自行车不能重复被使用
        used_bike = set()
        for pairs in bucket:
            for i, j in pairs:
                # 要worker 还没被分配车，并且分配的车还没有被使用时
                if result[i] == -1 and j not in used_bike:
                    result[i] = j
                    used_bike.add(j)
        return result


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        pairs = []
        for i, (w_x, w_y) in enumerate(workers):
            pairs.append([])
            for j, (b_x, b_y) in enumerate(bikes):
                distance = abs(w_x - b_x) + abs(w_y - b_y)
                # 记录每一个worker 对 每一个bike 的距离
                heapq.heappush(pairs[-1], (distance, i, j))
        # use a global heap to keep track of the nearest bike for each worker
        # 把i留着 是因为之后可以通过i 继续找下一个bike
        heap = [(heapq.heappop(c), i) for i, c in enumerate(pairs)]
        heapify(heap)

        result = [-1] * len(workers)
        used_bikes = set()

        while heap and len(used_bikes) < len(workers):
            # 每次拿出距离最短的
            (_, i, j), index = heapq.heappop(heap)
            if result[i] == -1 and j not in used_bikes:
                result[i] = j
                used_bikes.add(j)
            # 这说明 当前bike被别人占用了，拿下一个bike 放进去
            elif result[i] == -1:
                heapq.heappush(heap, (heapq.heappop(pairs[index]), index))
        return result