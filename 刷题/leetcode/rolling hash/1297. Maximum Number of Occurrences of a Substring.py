class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        n = len(s)
        # 储存最后结果对应的frequency
        dic = collections.Counter()
        # 储存窗口中的字母
        counter = collections.Counter()
        result = count = 0
        mod = 10 ** 9 + 7
        # 窗口内的编码
        code_s = 0
        base = 26
        total_base = base ** minSize
        # 计算最小窗口的code
        for i in range(minSize):
            counter[s[i]] += 1
            if counter[s[i]] == 1:
                count += 1
            code_s = (code_s * base + (ord(s[i]) - ord("a"))) % mod
        # # 只需要数最小的size就行， 因为大的子串必然包括小的子串
        for i in range(1, n - minSize + 1):
            # 只要窗口内的字母小于最大的letter 才可以更新result
            if count <= maxLetters:
                dic[code_s] += 1
                result = max(result, dic[code_s])
            # 去掉左边，移动窗口一格
            counter[s[i - 1]] -= 1
            if counter[s[i - 1]] == 0:
                count -= 1
            # 加上右边的字母
            counter[s[i + minSize - 1]] += 1
            # 计算新括号内的字母
            if counter[s[i + minSize - 1]] == 1:
                count += 1
            # 计算新括号的code
            code_s = (code_s * base - ((ord(s[i - 1]) - ord("a")) * total_base) + (
                        ord(s[i + minSize - 1]) - ord("a"))) % mod
        # 最后一个还要计算一次
        if count <= maxLetters:
            dic[code_s] += 1
            result = max(result, dic[code_s])
        return result


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        if not s:
            return 0
        # 建立字典
        dic = collections.Counter()
        n = len(s)
        result = 0
        # 只需要数最小的size就行， 因为大的子串必然包括小的子串
        for i in range(n - minSize + 1):
            temp = s[i : i + minSize]
            check = set(temp)
            if len(check) <= maxLetters:
                dic[temp] += 1
                result = max(result, dic[temp])
        return result