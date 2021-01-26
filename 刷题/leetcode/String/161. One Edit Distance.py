class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = len(s)
        n = len(t)
        if abs(m - n) > 1:
            return False
        for i in range(min(m, n)):
            if s[i] != t[i]:
                if m == n:
                    # 如果相等，那么使用replace
                    # 看当前字符后面的string 是不是都相等
                    return s[i + 1:] == t[i + 1:]
                elif m > n:
                    # 如果s 大于 t， 用delete
                    # 需要看s 后面的string 是不是等于 t 的string 包括当前的
                    return s[i + 1:] == t[i:]
                else:
                    # 如果s 小于t 用insert
                    # 那么需要看s当前的string， 是不是等于t后面的stirng
                    return s[i:] == t[i + 1:]
        # 如果都相等，看两个字符串是不是相差1
        return abs(m - n) == 1
