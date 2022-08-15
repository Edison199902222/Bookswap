class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        dic = collections.defaultdict(set)
        for word1, word2 in pairs:
            dic[word1].add(word2)
            dic[word2].add(word1)
        for i in range(len(words1)):
            word1, word2 = words1[i], words2[i]
            if word1 != word2 and word2 not in dic[word1]:
                return False
        return True
'''
储存就 然后检查
'''