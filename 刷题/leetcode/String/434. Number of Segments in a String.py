'''
如何检查 一个正确的单词
只要 单词出现前 是空格 并且 目前这个字符 不是空 那么这就是一个单词的开始 res+=1
或者 如果这是句子的开头 index = 0 并且目前进来的字符不是空的话 那么也是一个单词的开始 res需要+=1
'''

class Solution:
    def countSegments(self, s: str) -> int:
        max_number = 0
        for i in range(len(s)):
            if (i == 0 or s[i - 1] == " " ) and s[i] != " ":
                max_number += 1
        return max_number