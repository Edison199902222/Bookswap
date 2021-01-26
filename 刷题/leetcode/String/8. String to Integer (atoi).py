'''
首先 我们用strip 去掉前后空格 然后检查是不是为空
如果为去掉空格后 里面没有东西的话 那么我们直接返回0
然后我们就检查第一位 是正号还是负号的问题 如果是正号 我们sign 不变 如果是负号 我们sign需要变成-1 并且index 需要+1 因为字符串第一位我们已经检查过了
然后遍历字符串 如果发现不是数字的 就直接break
如果是数字的话 那么我们就把数字放进我们res之中
一旦发现res 超过了我们的max——int 的话 那也需要break
最后一步 sign*res 得到最终结果
然后 判断 sign*res 超过了我们的两个边界还是没有超过
'''

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        min_int = -2147483648
        max_int = 2147483647
        if len(str) == 0:
            return 0
        sign = 1
        index = 0
        res = 0
        if str[0] == "+":
            index += 1
        elif str[0]== "-":
            index += 1
            sign = -1
        while index < len(str):
            if not str[index].isdigit():
                break
            res = res*10 + ord(str[index]) - ord("0")
            if res > max_int:
                break
            index += 1
        return min( max(sign*res, min_int), max_int)