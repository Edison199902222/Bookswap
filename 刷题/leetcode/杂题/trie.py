import collections


class Node:
    def __init__(self):
        self.child = collections.defaultdict(Node)
        self.index = -1

class Trie:
    def __init__(self):
        self.root = Node()

    def add_word(self, word, i):
        node = self.root
        for w in word:
            node = node.child[w]
            node.index = i

    def search(self, word):
        node = self.find(word)
        if node.index != -1:
            return node.index
        else:
            return -1

    def find(self, word):
        node = self.root
        for w in word:
            if w not in node.child:
                return node
            node = node.child[w]
        return node


def find(arr):
    result = []
    trie = Trie()
    for i in range(len(arr)):
        if i == 0:
            result.append(0)
            trie.add_word(arr[i], i + 1)
        else:
            index = trie.search(arr[i])
            if index == -1:
                result.append(i)
            else:
                result.append(index)
            trie.add_word(arr[i], i + 1)
    return result

def main():
    arr = ['0101101010111110001001110', '1001101101100000', '100000101111110100101101000101', '011010011100101011', '001000110100101100001001111',
'0010101', '110011011000001', '10000000101101100100', '0011', '0000001010001000011111011']
    result = find(arr)
    print(result)
main()

