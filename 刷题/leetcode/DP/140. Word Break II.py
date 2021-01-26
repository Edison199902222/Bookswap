class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.memo = {}
        # 记忆化搜索
        wordDict = set(wordDict)
        return self.dfs(0, wordDict, s)

    def dfs(self, index, wordDict, s):
        if index == len(s):
            return []

        if index in self.memo:
            return self.memo[index]

        result = []
        # 遍历当前start， 到s 的结尾
        # 尝试找出在word dict 中的单词
        for i in range(index, len(s)):
            substring = s[index: i + 1]
            if substring in wordDict:
                sub_result = self.dfs(i + 1, wordDict, s)
                if sub_result:
                    for string in sub_result:
                        result.append(substring + " " + string)
                # 避免else 情况， 如果是else的话，最后一个不满足的话， 还是会添加进result中

        # 避免如果是空的情况的话，如果是空的情况， 要检查最后整个单词是不是在word dict 中， 如果是的话，把整个放进result中
        # 如果后面不匹配的话， 只有后面整个单词匹配才行
        if s[index:] in wordDict:
            result.append(s[index:])

        self.memo[index] = result
        return result


"""
这题已经不是我们前面看的那种简单的回溯了。也不能套用前面那些回溯的模版
https://www.youtube.com/watch?v=JqOIRBC0_9c
https://leetcode.com/problems/word-break-ii/discuss/44311/Python-easy-to-understand-solution
答案：
其实这题是一步步拆分来做的
1.memo是一个字典，他的 key是s中的字符串，value是这个字符串能拆分成wordDict的什么形式(部分答案)
    例如： key = anddog , value = and dog || 
  它的作用是，记录当前字符串片段的可能分解(部分答案)

2.主循环里有一个res = [],准备保留着最终结果，然后for循环把dict里的每一个单词(word)都拿出来去尝试，
然后把,s - word部分再继续递归，试图返回一个部分结果的res （resultofRest），来与word进行拼接，来形成最终答案

3.剩下的一些都是一些为这些递归准备的限制条件
"""