class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # 由于speeds和minEfficiency都是根据选择的工程师变化而变化的，因此需要控制其中一个变量递减才能比较出结果最大值。
        # 取决于最小的效率， 所以可以想到 排序效率，对效率进行枚举，定住效率，选速度，在当前这么多工程师中，选之前的k - 1 个工程师
        # 加上当前效率最低的工程师来计算result，每次新进来一个工程师，把前面速度最小的工程师去掉
        # 由于是根据效率从大到小排序的，因此计算表现值的效率只会小于或等于上次计算的表现值，而速度和可能大于或小于或等于上次表现值。
         # 同时，当工程师数大于k时，选择速度最慢的工程师删除
        temp = []
        for i in range(len(efficiency)):
            temp.append([efficiency[i], speed[i]])
        temp.sort(reverse = True)
        heap = []
        cur_sum = 0
        result = 0
        for i in range(len(temp)):
            heapq.heappush(heap, (temp[i][1], i))
            cur_sum += temp[i][1]
            if len(heap) > k:
                cur_sum -= heapq.heappop(heap)[0]
            result = max(result, cur_sum * temp[i][0])
        return result % (10 ** 9 + 7)