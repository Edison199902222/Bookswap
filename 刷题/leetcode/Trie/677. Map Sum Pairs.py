class TrieNode(object):
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        # 设置weight
        self.weight = 0


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word, weight):
        node = self.root
        for i in range(len(word)):
            # 把所有的node 都加上weight
            node = node.child[word[i]]
            node.weight += weight

    def search(self, word):
        node = self.root
        for w in word:
            if w not in node.child:
                return 0
            node = node.child[w]
        return node.weight

    # 如果单词已经出现过的话，就要重新更新weight， 把所有weight 都改成新的weight
    def update(self, word, weight):
        node = self.root
        for w in word:
            node = node.child[w]
            node.weight = weight


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()
        # 用来记录单词有没有出现过
        self.visited = set()

    def insert(self, key: str, val: int) -> None:
        trie = self.trie
        if key in self.visited:
            trie.update(key, val)
        else:
            trie.add_word(key, val)
            self.visited.add(key)

    def sum(self, prefix: str) -> int:
        trie = self.trie
        return trie.search(prefix)

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)