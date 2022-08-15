class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        result = 0
        count = 0
        for i in range(1, n + 1):
            # 每增加一个1 会多出来 count 这么多个
            if s[i - 1] == "1":
                count += 1
                result += count
            else:
                count = 0
        return result % (10 ** 9 + 7)

class Solution:
    def numSub(self, s: str) -> int:
        count = 0
        result = 0
        for i in range(len(s)):
            if s[i] == "1":
                count += 1
            else:
                # 等差数列求和公式
                # 如果一个字符串长为n，且全为1，那么符合条件的子字符串的个数就是1+2+3+。。。+n = (n+1)*n/2
                # 长度为1的有n个，长度为2的有n-1个。。。长度为n的有1个
                result += count * (1 + count) // 2
                count = 0
        result += count * (1 + count) // 2
        return result % (10 ** 9 + 7)