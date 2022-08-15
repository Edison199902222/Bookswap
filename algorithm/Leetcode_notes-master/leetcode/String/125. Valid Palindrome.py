class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return True
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
'''
双指针 
从头部 跟 尾部 开始扫
开始循环 如果遇到不是字母的话 那么我们就需要移动指针 指向字母才可以开始判断
'''

if __name__ == "__main__":
    solution= Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))