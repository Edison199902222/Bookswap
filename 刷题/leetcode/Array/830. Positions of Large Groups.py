class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        left = 0
        result = []
        for right in range(len(S)):
            if right == len(S) - 1 or S[right] != S[right + 1]:
                if right - left + 1 >= 3:
                    result.append((left,right))
                left = right + 1
        return result
'''
还是运用了同向双指针
我们只需要考虑 什么时候计算 整个字符串的长度
要么就是 我们的right 指针 指向了整个S的最后一位 要么就是 right的下一个 跟现在的字符 不相等
这时候 我们就要检查 整个 sub string 长度是不是大于等于3的
如果大于等于3 那么我们就添加进result中 
并且 我们的left 指针需要更新 因为这时候需要重新计算新的 substring
'''