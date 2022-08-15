class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        index1 = None
        index2 = None
        result = float("inf")
        for i in range(len(words)):
            if words[i] == word1:
                index1 = i
            elif words[i] == word2:
                index2 = i
            if index1 != None and index2 != None:
                result = min(result, abs(index1 - index2))
        return result
'''
遍历一遍words list，找到word1就更新pointer1，找到word2就更新pointer2。
每找到任何一个word，就计算出当前distance，跟min打擂台。

'''