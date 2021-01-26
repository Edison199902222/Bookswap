class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        res = 0
        set_word = [0 for i in range(n)]
        for i in range(len(words)):
            for j in words[i]:
                set_word[i] = set_word[i] | (1 << ord(j) - ord("a"))
        for i in range(n - 1):
            for j in range(i + 1, n):
                if set_word[i] & set_word[j] == 0:
                    res = max(res, len(words[i])*len(words[j]))
        return res
'''
把每一个单词，都转化为二进制数，规则是把26个英文字母映射到二进制数的每一位，例如a映射到第0位、b第一位。如果一个数是abc，那么这个数是00，0000，0000，0000，0000，0000，0111。
进行这个操作是通过二进制移位，然后或上本身，word |= 1 << ord(letter) - ord('a')，
当letter是b时，ord（letter）-ord（'a'）等于1，把1往左移1位（其实就是把第二位变成了1、即存在b，第二位变为1）
两个数不同是通过a & b = 0来实现的，因为没有相同字母，意味着两个数在任意一位上，都不同（0和1），而0&1 = 0

'''