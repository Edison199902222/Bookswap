class Node:
    def __init__(self):
        self.child = collections.defaultdict(Node)
        self.end_word = False
        # 要根据hot 来排名
        self.hot = 0


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word, times):
        node = self.root
        for w in word:
            node = node.child[w]
        node.end_word = True
        # 减去times， 这样等下sort 可以让times越大的在前面，并且 也会按照字符顺序排名
        node.hot -= times

    def find(self, word):
        node = self.find_node(word)
        result = []
        if node:
            self.dfs(node, "", result)
            # 把所有后缀放进result后，还要加上前缀 才是完整的
            for i in range(len(result)):
                result[i][1] = word + result[i][1]
            temp = [x[1] for x in sorted(result)][:3]
            return temp
        return result

    def dfs(self, node, path, result):
        if node.end_word:
            result.append([node.hot, path])

        for w in node.child:
            self.dfs(node.child[w], path + w, result)
        return

    def find_node(self, word):
        # 找node
        node = self.root
        for w in word:
            if w not in node.child:
                return None
            node = node.child[w]
        return node


class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.trie = Trie()
        self.prevfix = ""
        for i in range(len(sentences)):
            self.trie.add(sentences[i], times[i])

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        root = self.trie
        if c != "#":
            self.prevfix += c
            return root.find(self.prevfix)
        elif c == "#":
            root.add(self.prevfix, 1)
            self.prevfix = ""
            return []

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)