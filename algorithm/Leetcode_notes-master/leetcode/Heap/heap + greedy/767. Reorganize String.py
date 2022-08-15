import heapq
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        # 第一步 算出 数字出现的次数
        count = collections.Counter(S)
        heap = []
        # 第二步 放进heap中
        for key, value in count.items():
            heapq.heappush(heap, (-value, key))
        temp = []
        result = []
        # 第三步 每次把最常出现的 跟 第二常出现的放进result
        # 因为最常出现的数字， 最有可能相邻，所以先处理最常出现的
        while len(result) < len(S):
            while temp:
                heapq.heappush(heap, temp.pop())
            for i in range(2):
                if not heap and temp:
                    return ""
                if heap:
                    frequency, word = heapq.heappop(heap)
                    result.append(word)
                    frequency += 1
                    if frequency < 0:
                        temp.append((frequency, word))
        return "".join(result)

