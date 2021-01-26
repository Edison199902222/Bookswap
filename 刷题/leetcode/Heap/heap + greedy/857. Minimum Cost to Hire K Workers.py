class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        temp = []
        # 思路： 每个工人的工资都需要满足两个条件，并且总会有一个工人是刚好满足最低工资的
        # 所以，我们用 工资 / 质量 这就是每个工人的价值，然后枚举 某个工人刚好满足最低工资
        # 就可以得到某个工人的价值， 所有小于当前工人的价值的工人，都会满足最低工资
        # 而所有 高于当前工人的价值的工人，都不会满足最低工资
        # 原理： 所有的工资都是基于某一个工人的 工资/ 质量来的，第一条rule 如果第y个工人的质量 是 第x工人质量的 2倍，
        # 那么我们工资的价钱就要是 x 工人价钱的2 倍
        # 其实等价于y 工人的工资 基于 x 的 工资/ 质量 来的

        for i in range(len(quality)):
            temp.append([wage[i] / quality[i], quality[i], wage[i]])
        temp.sort()
        # 维护一个最大堆，里面放入质量， 每次heap中是当前所有的质量，如果heap中 worker 人数超出k
        # 那么需要把之前worker 中，质量最大的pop掉，每次选质量最小的k - 1 个 和 当前worker
        heap = []
        sums = 0
        result = float("inf")
        for i in range(len(temp)):
            ratio, q, w = temp[i][0], temp[i][1], temp[i][2]
            sums += q
            heapq.heappush(heap, -q)
            if len(heap) > K:
                sums += heapq.heappop(heap)
            if len(heap) == K:
                result = min(result, ratio * sums)
        return result

