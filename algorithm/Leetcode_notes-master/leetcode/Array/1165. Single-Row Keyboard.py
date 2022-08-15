class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        dic = {}
        for i in range(len(keyboard)):
            dic[keyboard[i]] = i
        last_index = 0
        result = 0
        for i in word:
            result += abs(last_index - dic[i])
            last_index = dic[i]
        return result
