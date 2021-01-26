'''
用一个字典
先遍历 然后同时遍历s 跟t 看s的字母 如果他在字典中 并且如果字典的value不是我们的ti 那就return false
如果不在的话 还需要查看 ti是不是以及作为字典重的value了 如果是的话 也需要return false
然后添加进字典
'''


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None or t is None: return True
        hashtable = {}
        for i in range(len(s)):
            si = s[i]
            ti = t[i]
            if si in hashtable:
                if hashtable[si] != ti:
                    return False
            else:
                if ti in hashtable.values():
                    return False
                hashtable[si] = ti
        return True
