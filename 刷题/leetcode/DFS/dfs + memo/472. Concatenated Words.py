class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # Time: O(n*l)
        # Space: O(n)
        # 跟140 很像
        self.memo = {}
        word_set = set(words)
        result = []
        for word in words:
            if self.dfs(word, word_set):
                result.append(word)
        return result

    def dfs(self, word, word_set):
        if word in self.memo:
            return self.memo[word]
        result = False
        # 尝试每次把words 拆成两半，要考虑后一半是一个word 的情况
        # word - 1 是因为，如果拿整个word 肯定在里面, 所以不能取整个word 来判断
        # 所以 要多判断一种情况，一个word 直接可以拆成两个word 同时在里面的情况
        for i in range(len(word) - 1):
            if word[:i + 1] in word_set and (word[i + 1:] in word_set or self.dfs(word[i + 1:], word_set)):
                result = True
                break
        self.memo[word] = result
        return result