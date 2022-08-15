class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 题目要求 找到一个sub sequence， 每个字母只出现一次 必须包含所有出现过的字母，并且字典顺序尽量小
        # 字典顺序指的是字典序是指从前到后比较两个字符串大小的方法
        # 首先比较第 1 个字符，如果不同则第 1 个字符较小的字符串更小；
        # 如果相同则继续比较第 2 个字符 …… 如此继续，比较整个字符串的大小。

        # 思路，根据题意，如果一个字母从始至终只出现了一次，那么这个字母肯定要被选上
        # 其次，如果一个字母出现多次，那么我们可以决定留下哪一个， 决定留下哪一个取决于后面的字母是否大于当前字母
        # 如果后面的字母小于当前字母，并且当前字母出现多次的话，自然当前字母可以被pop掉
        # 如果当前字母已经在result中了，那么证明已经维护了一个有序的result， 当前字母不能再放进去，所以跳过
        counter = collections.Counter(s)
        result = []
        for i in range(len(s)):
            if s[i] not in result:
                while result and s[i] < result[-1] and counter[result[-1]] > 0:
                    result.pop()
                result.append(s[i])
            counter[s[i]] -= 1
        return "".join(result)