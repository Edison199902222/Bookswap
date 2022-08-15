'''
不用 Trie，直接使用哈希表的方法
我们使用set 来代表前缀
先遍历word 把每一个前缀放进prefix set中
然后遍历board
上下左右搜索，
每次 如果发现当前word不是前缀的话 直接return
如果发现当前word 在我们的words set中的话 把它添加进结果中
然后上下左右搜索 每次把新的坐标 放进visited 中
'''
import collections


class TrieNode(object):
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = TrieNode()
        words = set(words)
        for word in words:
            node = root
            for w in word:
                node = node.child[w]

        self.result = set()
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                node = root
                if board[i][j] in node.child:
                    visited[i][j] = True

                    self.dfs(node.child[board[i][j]], str(board[i][j]), board, i, j, words, visited)
                    visited[i][j] = False

        return self.result

    def dfs(self, node, cur_word, board, i, j, words, visited):

        if cur_word in words:
            self.result.add(cur_word)

        for new_x, new_y in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
            if new_x < 0 or new_y < 0 or new_x >= len(board) or new_y >= len(board[0]) or visited[new_x][new_y] or \
                    board[new_x][new_y] not in node.child:
                continue
            visited[new_x][new_y] = True
            self.dfs(node.child[board[new_x][new_y]], cur_word + board[new_x][new_y], board, new_x, new_y, words,
                     visited)
            visited[new_x][new_y] = False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return []
        trie = collections.defaultdict()
        # 创建字典树
        for word in words:
            t = trie
            for i in range(len(word)):
                # 前缀不在的话 才能创建，不然不需要创建
                if word[i] not in t:
                    t[word[i]] = {}
                t = t[word[i]]
            t["#"] = {}
        self.result = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie:
                    visited = set()
                    visited.add((i, j))
                    self.search(board, trie[board[i][j]], i, j, visited, board[i][j])
        return self.result

    def search(self, board, trie, i, j, visited, cur_word):
        if "#" in trie:
            self.result.add(cur_word)
        for new_x, new_y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]) and (new_x, new_y) not in visited and \
                    board[new_x][new_y] in trie:
                visited.add((new_x, new_y))
                self.search(board, trie[board[new_x][new_y]], new_x, new_y, visited, cur_word + board[new_x][new_y])
                visited.remove((new_x, new_y))


