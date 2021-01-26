'''
就遍历 用两个指针
每次 检查两个字符串是否相等 如果不想等 直接return之前相等的字母
最后 要return list的第一个 是因为如果 strs 只是一个字符串 例如【"a"】 的时候 我们就需要直接return
'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None or len(strs) == 0:
            return ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1,len(strs)):
                if i == len(strs[j]) or c!= strs[j][i]:
                    return strs[0][:i]
        return strs[0]