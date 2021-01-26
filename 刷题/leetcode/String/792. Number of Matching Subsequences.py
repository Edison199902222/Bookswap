class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        dic = collections.defaultdict(list)
        # 第一步， 根据首字母分配
        for word in words:
            dic[word[0]].append(word)
        result = 0
        # 第二步，遍历s， 把每一个字母 放到dic中 寻找对应的字符串列表
        for c in S:
            matching_list = dic[c]
            dic[c] = []
            # 第三步， 遍历候选字符串列表， 去掉首字母，再放进dic中
            for word in matching_list:
                # 第四部 检查， 如果某个单词长度为1， 说明单词已经遍历完，证明是subsequence
                if len(word) == 1:
                    result += 1
                else:
                    dic[word[1]].append(word[1:])
        return result