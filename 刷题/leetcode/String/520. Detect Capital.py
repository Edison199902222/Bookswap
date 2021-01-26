class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word == word.lower() or word == word.upper():
            return True
        for i in range(1,len(word)):
            if word[i] == word[i].upper():
                return False
        return True
'''
三种情况 才被允许
首先我们检查 是不是全是大写 或者 全是小写
然后 我们就剩下一种情况了
我们不关心第一个字母是不是大写 或者是不是小写 所以我们从第二个字母开始检查
如果发现一个大写字母 那就是错的
'''