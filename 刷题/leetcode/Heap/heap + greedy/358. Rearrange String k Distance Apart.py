class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        # 第一步 创建字母出现的次数表
        count = collections.Counter(s)
        heap = []
        # 第二步 放进heap中，最常出现的先pop
        for key, value in count.items():
            heapq.heappush(heap, (-value, key))
        result = []
        # 第三步 创建temp 记录还需要添加进result的字母
        temp = []
        while len(result) < len(s):
            # 上一轮未使用完的字母，这一轮需要继续使用
            while temp:
                heapq.heappush(heap, temp.pop())
            # 第四步， 添加字母进result，需要k这么多个间隔不能使用同一个字母
            for i in range(max(k, 1)):
                # 检查heap 与 temp中还有之前用过的字母， 没有的话说明同一个字母不能间隔k
                if not heap and temp:
                    return ""
                if heap:
                    frequency, word = heapq.heappop(heap)
                    result.append(word)
                    frequency += 1
                    # 未使用完的话
                    if frequency < 0:
                        temp.append((frequency, word))
        return "".join(result)
