'''
先创建一个字典 把chars的字符 数出来
然后 遍历 words list
对于每一个单词 创建一个字典 数每个字符出现的次数
然后对字典中每一个字符 与 chars的字典 进行比较
如果当前字符 不在chars 字典 中 或者 chars中 当前字符出现的次数 是小于 当前word 字典 中 出现的次数的
说明不满足条件 说明 这个单词 并不可以 组成 chars
如果满足 则加入res
'''

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        dic_chars = collections.Counter(chars)
        res = 0
        for word in words:
            dic_word = collections.Counter(word)
            is_good = True
            for key in dic_word:
                if key not in dic_chars  or dic_chars[key] < dic_word[key]:
                    is_good = False
                    break
            if is_good:
                res += len(word)
        return res