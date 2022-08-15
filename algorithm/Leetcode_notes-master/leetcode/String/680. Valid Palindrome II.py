class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) -1
        while left < right:
            if  s[left] != s[right]:
                substring1 = s[left:right]
                substring2 = s[left+1:right+1]
                return substring1 == substring1[::-1] or substring2 == substring2[::-1]
            left += 1
            right -= 1
        return True
if __name__ == "__main__":
    solution = Solution()
    print(solution.validPalindrome("abca"))
'''
可以用双指针办法去判断一个字符串
首先 我们用两个指针 字符串首 和字符串尾
检查并且缩小 看看两个指针指向的字符 是不是相等 因为如果 外面都不是 不相等了 再检查里面也没用
直到遇到不相等的情况 
遇到不相等的情况 那么我们尝试去删除 左边的字符 或者删除 右边的一个字符 
再次检查 删除过后是不是一个回文 如果不是 return False
最后要return True 因为有可能一直遇到相等的情况
'''