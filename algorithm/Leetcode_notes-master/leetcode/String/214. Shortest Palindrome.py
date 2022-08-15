
'''
list1 = [1,2,3,4,5,6,7,8,9]
print(list1[-3:])
[7, 8, 9]
print(list1[:-4])
[1, 2, 3, 4, 5]
先从后往前找回文的
然后 用 j - len（s）会分成两部分
第一部分 我们不知道是不是回文  第二部分 我们知道 是回文的后缀
adcba 分成 ad  和 cba
然后反转cba
abc  + self（ad） + cba

'''

'''
从后往前每次减去一个字符后子串是否为回文串。
答案为将减去的部分翻转后接入最前面
'''
class Solution:
    """
    @param str: String
    @return: String
    """

    def shortestPalindrome(self, str):
        # Write your code here
        if not str or len(str) == 0:
            return ""

        n = len(str)
        for i in range(n - 1, -1, -1):
            substr = str[:i + 1]
            if self.isPalindrome(substr):
                if i == n - 1:
                    return str
                else:
                    return (str[i + 1:][::-1]) + str[:]

    def isPalindrome(self, str):
        left, right = 0, len(str) - 1
        while left < right:
            if str[left] != str[right]:
                return False
            left += 1
            right -= 1

        return True

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s or len(s) == 0:
            return ""
        n = len(s)
        for i in range(n - 1, -1, -1):
            substring = s[:i + 1] #最少留一个， 当n = 0
            if self.is_palindrome(substring):
                if i == n - 1:
                    return s
                else:
                    return s[i + 1:][:: - 1] + s[:]
    def is_palindrome(self, s):
        return s == s[::-1]
if __name__ == "__main__":
    solution = Solution()
    print(solution.shortestPalindrome("aacecaaa"))