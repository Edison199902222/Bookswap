'''
i j 表示 从字符串i 到 j 是不是回文
用sbstring(i,j) 去记录最长的那个会文index
max_sub_len 记录最长回文的长度
然后初始化 dp
每个单个字母肯定是true 是回文
然后每个长度为2的字符串 如果 头跟尾相等 那也是true
然后遍历字符串 要记住 是len-2
每次查 如果头尾相等 并且 中间部分字符串也相等 那么设置为true
然后再检查 这个长度是不是大于我们之前的最长回文 如果大于 我们更新长度 和substring

遍历时
总体来说 我们每次取一段substring 检查是不是 回文 这个substring长度取决于每一次遍历的 step
第一次 step = 2 意思是 我们从长度为 3 的substring开始 从头检查到尾 从以第0 个字符开始第 长度为 3 的string 然后从第一个字符 长度为3 的string
然后第二次 step = 2 我们从长度为4 的substring 开始检查 从以第0 个字符开始第 长度为 4 的string 然后从第一个字符 长度为4 的string
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        n = len(s)
        dp = [[False for i in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i] = True
        max_length, start, end = 1, 0, 0
        for length in range(1, n):
            for i in range(n - length):
                j = i + length
                if s[i] == s[j] and (dp[i + 1][j - 1] or j - i <= 2):
                    dp[i][j] = True
                if dp[i][j] and length + 1 > max_length:
                    max_length = length + 1
                    start = i
                    end = j
        return s[start:end + 1]

'''
扩散法 
对于每个字符 我们都可以先检查当前的是不是回文
然后逐渐用 helper 函数 两个指针扩散开来 去检查 由当前字符开始 最长的回文
但是 有可能是由两个回文字符 开始扩散的 所以 对于每个字符串 要加一个特殊的情况
既要检查偶数情况 也要检查奇数情况
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_string = ""
        for i in range(len(s)):
            temp = self.find_palind(s, i, i)
            if len(temp) > len(max_string):
                max_string = temp
            temp = self.find_palind(s, i, i + 1)
            if len(temp) > len(max_string):
                max_string = temp
        return max_string
    def find_palind(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # left + 1 : right 是因为循环结束后 left指向的并不是paralind 的index，而是它左边一个， right也是
        # 如果越界情况，直接会返回空字符串
        return s[left + 1: right]
if __name__ =="__main__":
    solution = Solution()
    print(solution.longestPalindrome("aaaa"))