'''
两个指针
从最后面开始
一个指针会指向单词开始 一个指针指向单词结尾
每次遇到空格 添加进res里 并且更新最后一个指针 让它指向新的单词尾部
最后把res 加上 s【：right】 就行
'''


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 把前后空格，中间空格处理
        cur_s = self.make_space(s)
        # 处理完成后，多步翻转
        self.reverse(cur_s, 0, len(cur_s) - 1)
        left = 0
        right = 0
        while right < len(cur_s):
            if cur_s[right] == " ":
                self.reverse(cur_s, left, right - 1)
                left = right + 1
                right += 1
            elif right == len(cur_s) - 1:
                self.reverse(cur_s, left, right)
                right += 1
            else:
                right += 1
        return "".join(cur_s)

    def make_space(self, s):
        left, right = 0, len(s) - 1
        # 去掉前后的空格
        while left < len(s):
            if s[left] != " ":
                break
            left += 1
        while right >= 0:
            if s[right] != " ":
                break
            right -= 1
        result = []
        # 把中间的多个空格变成一个空格
        while left <= right:
            if s[left] != " ":
                result.append(s[left])
            elif result[-1] != " ":
                result.append(s[left])
            left += 1
        return result

    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1


class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ""
        s = list(" ".join(s.split()))
        n = len(s)
        self.reverse(s, 0, n - 1)
        left = 0
        for right in range(len(s)):
            if s[right] == " ":
                self.reverse(s, left, right - 1)
                left = right + 1
            elif right == len(s) - 1:
                self.reverse(s, left, right)
        return "".join(s)

    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1


if __name__ == "__main__":
    solution = Solution()
    Input = "the sky is blue"
    print(solution.reverseWords(Input))
