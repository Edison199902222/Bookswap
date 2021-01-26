class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        word_list = collections.Counter(s)
        odd_word = ""
        odd_number = 0
        cadidate = []
        for key, value in word_list.items():
            if value % 2 != 0:
                odd_word = key
                odd_number += 1
            for i in range(value // 2):
                cadidate.append(key)
        if odd_number > 1:
            return []
        self.result = []
        self.dfs(odd_word, cadidate, [])
        return self.result

    def dfs(self, odd_word, cadidate, path):
        if not cadidate:
            temp = "".join(path + [odd_word] + path[::-1])
            self.result.append(temp)
        pre = ""
        for i in range(len(cadidate)):
            if pre != cadidate[i]:
                path.append(cadidate[i])
                self.dfs(odd_word, cadidate[:i] + cadidate[i + 1:], path)
                path.pop()
            pre = cadidate[i]
'''
使用回溯法 我们是需要把前半部分找好，加上 odd word 加上 逆转前半部分就是满足题目要求的
先用字典 计数
然后统计 出现次数 为奇数 字符的数量，把所有字符 的数量 除2 放进我们的候选名单中，因为我们只拼接前半部分
统计完成后， 如果 odd number 超过了1，说明无法拼接成
然后 我们回溯法

首先 base case 我们每一次 从cadidate中拿走一个字符 放进path中，所以 如果cadidate 中 什么都没有了，那说明我们拼接成功了 
然后 我们用pre 指向 上一次 相同的位置 用了哪一个字符拼接， 因为我们要保证 没有重复的拼接的单词的话， 相同位置不能让相同的字母拼接。
然后把当前从cadidate 遍历到的字符 尝试放进path 中，进行下一次递归
'''