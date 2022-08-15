'''
同向双指针
用一个字典去记录每个字母最后出现的index
然后每次判断 如果当前字符 出现过 并且 是在start 之后出现过的话 说明 是不合法的
我们就移动start
如果没有在start之后出现过 那么说明 目前范围里 这个字符是第一次出现 那么我们就更新次数
为什么start <= dic[char]
是因为 只有重复的字母 在start之后重复 才算重复
比如 tmmzuxt start 现在在 第二个m 的位置 最后这个t不算重复

'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        check = set()
        left = 0
        result = 1
        for right in range(len(s)):
            while check and s[right] in check:
                check.remove(s[left])
                left += 1
            result = max(result, right - left + 1)
            check.add(s[right])
        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring("tmmzuxt"))