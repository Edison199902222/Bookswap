'''
先用字典去遍历words 找出每个单词出现的次数
然后用双指针
有点像窗口一样 一步一步扩散出去
i j 是 目前要找的这个string的长度
然后用k表示 是否找完了
每次 j都移动m个 m表示我们要找的单词长度
'''



class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if s is None or len(words) == 0: return
        n = len(words)
        m = len(words[0])
        dic = {}
        res =[]
        for i in range(len(words)):
            if words[i] not in dic:
                dic[words[i]] = 1
            else:
                dic[words[i]] += 1
        for i in range(len(s)-m*n+1):
            dic_copy = dic.copy()
            k = n
            j = i
            while k > 0:
                string = s[j:j+m]
                if string not in dic_copy or dic_copy[string] < 1:
                    break
                dic_copy[string] -= 1
                k -= 1
                j+=m
            if k == 0:
                res.append(i)
        return res
if __name__ == "__main__":
    solution = Solution()
    print(solution.findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"]))





