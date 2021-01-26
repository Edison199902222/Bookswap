class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        # 用字典记录前缀
        # 观察矩阵发现，如果要增加一行，那么只需要增加的word 的前缀，和当前 matrix 中 col 的前缀 一样就可以
        # 比如
        # [ "baba", 如果要增加 一行，那么就是要增加第index2 行，那么我么那就需要检查当前matrix 中第index 2 col
        #  "abat",] 也就是有前缀ba的话，那么就可以增加到 index 2 行
        dic = collections.defaultdict(list)
        # 把所有前缀 和对应的单词储存进dic
        for word in words:
            for i in range(len(word)):
                dic[word[:i]].append(word)

        n = len(words[0])
        self.result = []
        # 枚举第一行
        for word in words:
            self.dfs(dic, [word], n, 1)
        return self.result

    def dfs(self, dic, path, n, col):
        # 如果col 数量跟 n 相等，要返回
        if col == n:
            self.result.append(path)
            return
        prefix = ""
        # 找到当前col的前缀
        for i in range(len(path)):
            prefix += path[i][col]
        # 如果前缀在当前dic 中，那么可以添加下一行
        for cur_word in dic[prefix]:
            self.dfs(dic, path + [cur_word], n, col + 1)
        return