class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        if sorted(list(s1)) != sorted(list(s2)):
            return False
        n = len(s1)
        for i in range(1, n):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[n - i:]) and self.isScramble(s1[i:], s2[:n - i]):
                return True
        return False
'''
用dfs + 减枝
base case：首先如果两个string的长度不相等 肯定不是 然后 如果长度相等 并且两个string是一样的 直接return true
然后如果 排序后 两个 string 还是不相等的话 肯定也不是 scramble的 如果是scrambke的话 虽然顺序变了 但是排序后 肯定是一样的
中间处理 ： 从1 到 s1的长度 开始枚举， 枚举是每一次怎么把string分开， 从长度1 开始分 左边为长度为1的string 右边是 总长度-1 的string
然后 在里面dfs 并且判断 如果 递归下去 s1的前半段substring 跟 s2 的前半段substring 一样 并且 s1的后半段substring 也和 s2的后半段substring 是一样的 那return true
如果 s1的前半段substring 和s2的后半段substring是一样的 并且 s1 的后半段substring 跟s2的前半段substring是一样的 那么也return true
最后return false
'''