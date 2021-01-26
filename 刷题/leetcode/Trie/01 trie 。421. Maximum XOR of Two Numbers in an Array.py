class TrieNode:
    # 每次分成两个node 0或者1
    def __init__(self):
        self.one = None
        self.zero = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        cur_node = self.root
        for i in range(31, -1, -1):
            temp = word & (1 << i)
            if temp:
                if not cur_node.one:
                    cur_node.one = TrieNode()
                cur_node = cur_node.one
            else:
                if not cur_node.zero:
                    cur_node.zero = TrieNode()
                cur_node = cur_node.zero


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        for num in nums:
            trie.add_word(num)
        result = 0
        # 想要异或的结果最大， 那么对于每个数字来说，如果存在一个每一位都与当前位相反的数字的话，那么就能得到当前数字跟另一个数字异或的最大值
        # 用0 1 trie 去找这个数
        for num in nums:
            cur_node = trie.root
            cur_val = 0
            for i in range(31, -1, -1):
                temp = num & (1 << i)
                if cur_node.one and cur_node.zero:
                    if temp:
                        cur_node = cur_node.zero
                    else:
                        cur_node = cur_node.one
                    cur_val += (1 << i)
                else:
                    if (temp and cur_node.zero) or (not temp and cur_node.one):
                        cur_val += (1 << i)
                    cur_node = cur_node.one or cur_node.zero
            result = max(result, cur_val)
        return result

