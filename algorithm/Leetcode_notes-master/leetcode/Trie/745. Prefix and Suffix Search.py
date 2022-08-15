class TrieNode(object):
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.weight = []


class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        # 装当前prefix or suffix 的weight

    def add_word(self, word, i):
        node = self.root
        # 空串也有weight
        node.weight.append(i)
        for w in word:
            node = node.child[w]
            node.weight.append(i)

    # 返回word 对应的 weight
    def search(self, word):
        node = self.root
        for w in word:
            if w not in node.child:
                return []
            node = node.child[w]
        return node.weight


class WordFilter:

    def __init__(self, words: List[str]):
        # 创建前缀，后缀树
        self.prefix, self.suffix = Trie(), Trie()
        for i in range(len(words)):
            # 把前缀， 跟后缀放进树里面
            self.prefix.add_word(words[i], i)
            self.suffix.add_word(words[i][::-1], i)

    def f(self, prefix: str, suffix: str) -> int:
        # 在前缀树，跟后缀树 搜索当前的prefix， suffix 对应的weight
        prefix_weight = self.prefix.search(prefix)
        suffix_weight = self.suffix.search(suffix[::-1])
        i = len(prefix_weight) - 1
        j = len(suffix_weight) - 1
        while i >= 0 and j >= 0:
            # 只有 两个weight 一样，才能证明是同一个单词，从后往前遍历保证最大值
            if prefix_weight[i] == suffix_weight[j]:
                return prefix_weight[i]
            elif prefix_weight[i] < suffix_weight[j]:
                j -= 1
            else:
                i -= 1
        return -1

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)