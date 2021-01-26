class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        if not word:
            return [""]
        self.result = []
        self.dfs(word, 0, False, "")
        return self.result

    def dfs(self, word, index, flag, path):
        if index == len(word):
            self.result.append(path)
            return
        # 两种选择
        # 第一种选择， 把当前的字符 不缩进
        self.dfs(word, index + 1, False, path + word[index])
        # 第二种选择，缩进，但是需要保证之前的flag 是false 代表前一个没有缩进
        # 不能两个同时缩进
        if not flag:
            # 可以缩进的话， 我们就开始枚举缩进多长
            # 最小是1， 最长也可以缩进到 index 到 整个wrod 的长度 也就是 word - index + 1
            for length in range(1, len(word) - index + 1):
                self.dfs(word, index + length, True, path + str(length))
        return
