class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        banset = set(banned)
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        print(paragraph)
        count = {}
        paragraph = paragraph.split()
        for i in paragraph:
            if i.lower() not in count:
                count[i.lower()] = 1
            else:
                count[i.lower()] += 1

        ans, best = '', 0
        for word in count:
            if count[word] > best and word not in banset:
                ans, best = word, count[word]
        return ans

'''
先把所有符号用空格替代
再用split 变成list
然后用字典去数 出现了多少次
最后打擂台
'''