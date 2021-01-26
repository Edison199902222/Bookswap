class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
        return i == len(name)
'''
双指针的办法
i指向 name j 指向type
每次 检查 如果i 是有效的话 先看 两个字符是不是相同
是相同的话那么 i 就可以继续走 检查下一个
如果不是的话 那么我们就要看 不相同是不是出现在第一个位置 如果出现在第一个位置都不一样 那么肯定是错的
或者说 如果不相同的话 并且跟 自己之前的前一个字符也不相同 那肯定是错误的 因为在与 i 不同的情况下 我们需要跟自己本身之前的字符相同 才可以继续走下去
最后检查i 是不是走完全部的字符
'''