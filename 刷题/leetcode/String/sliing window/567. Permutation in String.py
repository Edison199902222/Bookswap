class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l1 = [0] * 26
        l2 = [0] * 26
        for i in s1:
            l1[ord(i) - ord("a")] += 1

        for i in range(len(s2)):
            l2[ord(s2[i]) - ord("a")] += 1
            if l1 == l2:
                return True
            if i >= len(s1) - 1:
                l2[ord(s2[i - len(s1) + 1]) - ord("a")] -= 1
        return False
'''
不使用第二个指针实现 sclicing window
性质就是 如果s2 有 s1的permutation的话， 那么在一段长度为s1 的s2中， 他们的字母出现的次数一定是一摸一样的
所以我们就遍历s2 用window找 在一段长度为 s1 的 s2中 能否找到这样一段
'''