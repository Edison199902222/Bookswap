class TrieNode(object):
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.end_word = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for w in word:
            node = node.child[w]
        node.end_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if word is None:
            return None
        node = self.root
        return self.dfs(word, 0, node)

    def dfs(self, word, index, node):
        # 到最后还需要检查 是不是结尾，因为有可能是前缀，而不是整个单词
        if index == len(word):
            return node.end_word
        if word[index] == ".":
            for i in node.child:
                if self.dfs(word, index + 1, node.child[i]):
                    return True
        else:
            if word[index] not in node.child:
                return False
            return self.dfs(word, index + 1, node.child[word[index]])

    '''
    用dfs搜索
    base case 如果word 没有了 我们就return 如果 node的标志变成true了
    我们就把res 变成true return
    然后每一次 查看word的 第一个字符 
    如果第一个字符是 点 的话 那么我们就要 遍历所有node 的child 的value 每一个都作为新的node 去尝试搜索接下来的word
    如果不是的话 我们要先判断word的第一个字符 是否在node child之中 如果不在 reutnr
    如果在的话 那么我们就把 它对应的 node的childe的value 作为新node
    继续dfs
    '''
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)