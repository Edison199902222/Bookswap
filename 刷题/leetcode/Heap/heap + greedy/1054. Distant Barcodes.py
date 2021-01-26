class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        # 第一步 算出 数字出现的次数
        count = collections.Counter(barcodes)
        heap = []
        # 第二步 放进heap中
        for key, value in count.items():
            heapq.heappush(heap, (-value, key))
        result = []
        # 第三步 每次把最常出现的 跟 第二常出现的放进result
        # 因为最常出现的数字， 最有可能相邻，所以先处理最常出现的
        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            result.append(first[1])
            result.append(second[1])
            if first[0] + 1 < 0:
                heapq.heappush(heap, (first[0] + 1, first[1]))
            if second[0] + 1 < 0:
                heapq.heappush(heap, (second[0] + 1, second[1]))
        if heap:
            temp = heapq.heappop(heap)
            result.append(temp[1])
        return result

