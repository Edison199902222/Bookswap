class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        stack = [ord(x) for x in str]
        for i in range(len(stack)):
            if stack[i] > 64 and stack[i] < 91:
                stack[i] += 32
        asw = [chr(x) for x in stack]
        return ''.join(asw)
'''
对于每个大小写字母 
大写字母 + 32 = 小写字母
然后遍历字符串 
先判断是不是大写字母
如果是 就+32 变成小写字母
不然就不改变
'''
if __name__ == "__main__":
    solution = Solution()
    print(solution.toLowerCase("Hello"))