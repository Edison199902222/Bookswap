'''
两个指针
一个从头往后遍历 一个从后往前遍历
第一个指针如果遇到元音 则不动
然后看第二个指针 移动 直到找到元音
然后进行交换
'''

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiou"
        s = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left].lower() not in vowels:
                left += 1
            elif s[right].lower() not in vowels:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left+=1
                right-=1
        return "".join(s)
if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseVowels("hello"))