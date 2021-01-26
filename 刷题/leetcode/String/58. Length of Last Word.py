'''
我们从后往前数
如果不为空的话 我们就开始计算length
只要不为空 长度就加1
如果这时候检查到一个空 说明最后一个单词结束了 需要return
为什么结束后还需要return length 因为如果为"" 空字符串的话 也需要return 0

'''
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s)-1
        length = 0
        while i >= 0 :
            if s[i] == " ":
                i-=1
            else:
                while i >= 0:
                    if s[i]!=" ":
                        length+=1
                        i-=1
                    else:
                        return length
        return length


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLastWord("Hello World"))
