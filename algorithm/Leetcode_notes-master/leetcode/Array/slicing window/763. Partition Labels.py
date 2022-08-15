class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = collections.Counter(s)
        result = []
        size = 0
        curent_counter = collections.Counter()
        prev = -1
        for i in range(len(s)):
            curent_counter[s[i]] += 1
            if curent_counter[s[i]] == counter[s[i]]:
                size += 1
            if size == len(curent_counter):
                result.append(i - prev)
                prev = i
                size = 0
                curent_counter = collections.Counter()
        return result

    class Solution:
        def partitionLabels(self, S: str) -> List[int]:
            # 记录最后一次出现的index
            dic = {c: i for i, c in enumerate(S)}
            prev = -1
            max_index = 0
            result = []
            for i in range(len(S)):
                # 记录最大的区间内最大的index
                max_index = max(max_index, dic[S[i]])
                # 如果区间内最后一个出现的index 等于当前i的，说明所有的letter找齐了
                if max_index == i:
                    result.append(i - prev)
                    prev = i
            return result
