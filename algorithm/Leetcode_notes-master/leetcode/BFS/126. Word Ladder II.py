'''
从 end 到 start 做一次 BFS，并且把距离 end 的距离都保存在 distance 中。
然后在从 start 到 end 做一次 DFS，每走一步必须确保离 end 的 distance 越来越近。

与另外一个代码中提前建立 index 不同，这里是在寻找下一个变换单词的时候，
再去获得对应的单词列表。一个单词最多有 L 个字符，每个字符有 25 种不同的变化（26个字母除掉这个位置上的字母），然后 check 一下在不在 dict 里就知道是不是 next word 了。
'''


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = set(wordList)
        wordList.add(beginWord)
        distance = {}
        self.bfs(endWord, distance, wordList)
        self.result = []
        self.dfs(distance, wordList, beginWord, endWord, [beginWord])
        return self.result

    def get_word(self, word, dic):
        result = []
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                new_word = word[:i] + c + word[i + 1:]
                # 一定要注意， 换字母有可能换成自己本身
                if new_word != word and new_word in dic:
                    result.append(new_word)
        return result

    # 算出 每一个单词 离 end 的距离
    def bfs(self, start, distance, word_list):
        distance[start] = 0
        queue = collections.deque([start])
        while queue:
            word = queue.popleft()
            for next_word in self.get_word(word, word_list):
                if next_word not in distance:
                    distance[next_word] = distance[word] + 1
                    queue.append(next_word)

    def dfs(self, distance, word_list, current, end, path):
        if current == end:
            self.result.append(path[:])
            return
        for word in self.get_word(current, word_list):
            if distance[word] != distance[current] - 1:  # 这表示的是 里endword 的距离， 如果下一个单词不会离endword 越来越近的话，就跳过
                continue
            path.append(word)
            self.dfs(distance, word_list, word, end, path)
            path.pop()