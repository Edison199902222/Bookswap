class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.dic = {}
        for i in range(len(words)):
            if words[i] not in self.dic:
                self.dic[words[i]] = [i]
            else:
                self.dic[words[i]].append(i) # 为什么 self.dic[words[i]] = self.dic[words[i]].append(i)会变成none

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1_index = self.dic[word1]
        word2_index = self.dic[word2]
        i = 0
        j = 0
        res = float("inf")
        while i < len(word1_index) and j < len(word2_index):
            res = min(res, abs(word1_index[i] - word2_index[j]))
            if word1_index[i] < word2_index[j]:
                i += 1 # 当 i < j的时候，我们如果求出更小的值呢，那么肯定是把更小的那个值 尽量的去接近更大的那个值 所以 移动i
            else:
                j += 1 # 当 i > j的时候，我们如果求出更小的值呢，那么肯定是把更小的那个值 尽量的去接近更大的那个值 所以 移动j
        return res
'''
time complex: O(n + m)
我们先把word中的所有字符 对应上它出现过的index 放进字典中
然后在 第二个函数中 
我们把 两个单词对应的 index list中拿出来
然后 用两个指针进行比较

'''

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
if __name__ == "__main__":
    obj = WordDistance(["WordDistance","shortest","shortest"])
    print(obj.shortest("WordDistance","shortest"))