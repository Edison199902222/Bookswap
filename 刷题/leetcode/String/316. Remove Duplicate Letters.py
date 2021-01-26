'''
先用字典遍历字符串 记录最后出现的位置
然后 再遍历一次字符串
如果 字符没有出现在result的时候 我们才能进行添加操作
进行添加操作之前  我们还需要判断 在这个字母之前的字母需不需要pop出来
判断条件是  1 result不为空 2 需要 当前字母 小于之前的字母 3 我们还需要判断 之前的那个字母 是不是后面还有 因为如果后面没有的话 我们就不能pop

'''


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_index = {}
        for i in range(len(s)):
            last_index[s[i]] = i
        result = []
        for i,ch in enumerate(s):
            if ch not in result:
                while result and ch < result[-1] and i < last_index[result[-1]]:
                    result.pop()
                result.append(ch)
        return "".join(result)
if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDuplicateLetters("cbacdcbc"))