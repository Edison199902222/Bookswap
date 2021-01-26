class Node():
    def __init__(self):
        self.child = collections.defaultdict(Node)
        self.end_word = False


class Trie():
    def __init__(self):
        self.root = Node()

    def add_word(self, words):
        node = self.root
        for w in words:
            node = node.child[w]
        node.end_word = True

    def search(self, letter):
        node = self.root
        i = len(letter) - 1
        while i >= 0:
            # 任何一个可以组成单词，并且是完整的 return
            if node.end_word:
                return True
            if letter[i] not in node.child:
                return False
            node = node.child[letter[i]]
            i -= 1
        # 当走完的时候，还需要检查 当前node 是不是走完了
        return node.end_word


class StreamChecker(object):
    # 题目意思是，当query 的时候，从后往前 看 letter 组成的单词有没有在words中
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.letter = []
        self.trie = Trie()
        for word in words:
            self.trie.add_word(word[::-1])

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.letter.append(letter)
        return self.trie.search(self.letter)

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)