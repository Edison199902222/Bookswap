'''
利用字典wmap保存单词 -> 下标的键值对
遍历单词列表words，记当前单词为word，下标为idx：
1). 若当前单词word本身为回文，且words中存在空串，则将空串下标bidx与idx加入答案

2). 若当前单词的逆序串在words中，则将逆序串下标ridx与idx加入答案

3). 将当前单词word拆分为左右两半left，right。

     3.1) 若left为回文，并且right的逆序串在words中，则将right的逆序串下标rridx与idx加入答案

     3.2) 若right为回文，并且left的逆序串在words中，则将left的逆序串下标idx与rlidx加入答案
'''


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # 思路：用两个for 直接暴力找每一个的话 时间复杂度是n 方 乘 k
        # 所以可以优化，遍历每个单词，把每个单词拆成左右两部分，因为如果可以拼成回文的话那么
        # 格式：单词 = left + right => left + right + left_reverse 如果 right 是回文的话，并且left 逆序对在words中
        # 或者 right_reverse + left + right 如果left 是回文的话，并且right 的逆序队也在words中
        # 时间复杂度下降到 k方乘n
        dic = {}
        # 找到word 对应index，方便后面加进result
        for index, word in enumerate(words):
            dic[word] = index
        result = []
        for index, word in enumerate(words):
            size = len(word)
            # 尝试把整个word分成left，right 两半，空串也算
            for i in range(size + 1):
                left = word[:i]
                right = word[i:]
                # 如果左半部分是回文，那么看右边的逆序对是不是在word中，如果在的话，可以拼接 right 的逆序 + 整个word 整个就是回文了
                if self.isvalid(left):
                    reversed_right = right[::-1]
                    if reversed_right in dic and dic[reversed_right] != index:
                        result.append([dic[reversed_right], index])
                # len(right) > 0 是因为，右边不能空串，不然在之后会重复添加
                if self.isvalid(right) and len(right) > 0:
                    reversed_left = left[::-1]
                    if reversed_left in dic and dic[reversed_left] != index:
                        result.append([index, dic[reversed_left]])
        return result

    def isvalid(self, s):
        return s == s[::-1]
