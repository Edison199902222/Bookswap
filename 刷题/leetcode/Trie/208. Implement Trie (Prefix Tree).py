class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class Trie:

    def __init__(self):
        # do intialization if necessary
        self.root = TrieNode()

    """
    @param: word: a word
    @return: nothing
    """

    def insert(self, word):
        # write your code here
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.word = True

    """
    @param: word: A string
    @return: if the word is in the trie.
    """

    def search(self, word):
        # write your code here
        node = self.find(word)
        if node is not None and node.word:
            return True
        else:
            return False

    def find(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                return None
            node = node.children[w]
        return node

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """

    def startsWith(self, prefix):
        # write your code here
        node = self.find(prefix)
        return node != None

