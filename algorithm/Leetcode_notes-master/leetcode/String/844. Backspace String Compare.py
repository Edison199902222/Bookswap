class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        i = len(S) - 1
        j = len(T) - 1
        back_s = 0
        back_t = 0
        while j >= 0 or i >= 0:
            while i >= 0 and (back_s > 0 or S[i] == "#"):
                if S[i] == "#":
                    back_s += 1
                else:
                    back_s -= 1
                i -= 1
            while j >= 0 and (back_t > 0 or T[j] == "#"):
                if T[j] == "#":
                    back_t += 1
                else:
                    back_t -= 1
                j -= 1
            if i == -1 or j == -1:
                return i == j
            if S[i] != T[j]:
                return False
            i -= 1
            j -= 1
        return True

'''
从后往前 遍历两个字符串
back s 与 back t 记录 两个字符串 各自需要几次倒退 每当遇到# 就说明 我们需要一次倒退 
用while 循环 去检查字符串 倒退有几次 并且 如果有倒退的话 那么我们就跳过当前字符
直到遇到稳定的字符
遇到稳定的字符后 我们第一个需要检查  
如果i 或者 j 是-1 的话 说明有一个字符串已经遍历完成了
我们检查 两个 字符串的index 是不是相等的 这样我们就知道另一个是不是也遍历完成了 
如果都遍历完成  return true 反之亦然
第二个 我们需要检查 如果都没有遍历完成的话， 我们就要看两个字符串 当前的字符是不是相等
不相等return false
然后 继续遍历
'''