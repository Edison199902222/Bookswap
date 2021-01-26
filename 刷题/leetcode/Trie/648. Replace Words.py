class TrieNode(object):
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.end_word = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for w in word:
            node = node.child[w]
        node.end_word = True

    def find_prefix(self, word):
        s = ""
        node = self.root
        # 遍历给出的word
        for w in word:
            # 先检查 是不是到头了，如果到头了 说明字典树此时的单词 s 就是 word 的前缀 直接break
            if node.end_word:
                break
            # 如果发现 任何一个字母 不在字典树中 直接return word
            if w not in node.child:
                return word
            # s 保存 当前合法的 字符
            s += w
            # 字典树进入下一层
            node = node.child[w]
        return s


class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        root = Trie()
        # 建立字典树
        for word in dict:
            root.add_word(word)

        result = []
        sentence = sentence.split()

        for char in sentence:
            node = root
            result.append(node.find_prefix(char))

        return " ".join(result)
