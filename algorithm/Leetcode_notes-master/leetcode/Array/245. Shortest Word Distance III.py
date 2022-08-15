class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        index = - 1
        minlength = float("inf")
        for i in range(len(words)):
            if words[i] == word1 or words[i] == word2:
                if index != -1 and word1 in [words[i], words[index]] and word2 in [words[i], words[index]]:
                    minlength = min(minlength, i - index)
                index = i
        return minlength
'''
跟1 通用的一个解法 
我们可以设置index 跟minlength 
然后遍历words
如果发现 当前字符 跟 我们的目标字符 word1 或者 word2相同的话
那么我们继续 检查 如果发现 index 不等于初始值（意思是 之前出现过word1 或者 word2 ）
并且 word1 跟 word2 都在 【word[i]，words[index]】 （这个意思是， 如果都在这个里面的话，说明我们之前的index 指向的word 跟我们现在i指向的word 不相同，也就是两个word 都找到了）
那么我们更新 min length
并且 把index 更新成 当前遍历的 i
'''