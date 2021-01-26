import collections
'''
bfs高频题
用一个wordset 去记录所有word 
为什么用set 因为避免重复回头走 每次如果newword在这个wordset之中 才可以添加quene里面去 并且把set里面的这个word删除掉
避免死循环 
然后我们 首先把beginword 跟 1 作为我们的开始 放进deque中
我们每一次先检查 如果当前pop出来的word 就是我们的endword的话 直接return
不然的话 我们就对于 word的每一个字符来说 我们去尝试用26个字母替换每一个元素
然后 如果 发现 新的单词 在我们的wordset 中 并且 不跟 我们替换之前的单词重复的话
我们就可以把它放进我们的 deque中 并且把wordset中 删除掉这个单词

'''

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        if not wordList:return 0
        wordset = set(wordList)
        bfs = collections.deque()
        bfs.append((beginWord,1))
        while bfs:
            word,length = bfs.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + char + word[i+1:]
                    if new_word in wordset and new_word != word:
                        wordset.remove(new_word)
                        bfs.append((new_word,length+1))
        return 0

if __name__ == "__main__":
    solution = Solution()
    print(solution.ladderLength("lost","miss",["most","mist","miss","lost","fist","fish"]))

