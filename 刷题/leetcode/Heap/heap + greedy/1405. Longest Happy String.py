class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        result = []
        heap = []
        if a != 0:
            heapq.heappush(heap, (-a, "a"))
        if b != 0:
            heapq.heappush(heap, (-b, "b"))
        if c != 0:
            heapq.heappush(heap, (-c, "c"))
        # 永远先安排most common substring
        while heap:
            frequency_first, word_first = heapq.heappop(heap)
            if len(result) >= 2 and result[-1] == result[-2] == word_first:
                # 如果heap中没有了，说明接下来无法再安排下去了，直接break 循环
                if not heap:
                    break
                frequency_second, word_second = heapq.heappop(heap)
                result.append(word_second)
                frequency_second += 1
                if frequency_second < 0:
                    heapq.heappush(heap, (frequency_second, word_second))
                heapq.heappush(heap, (frequency_first, word_first))
                continue
            result.append(word_first)
            frequency_first += 1
            if frequency_first < 0:
                heapq.heappush(heap, (frequency_first, word_first))
        return "".join(result)
