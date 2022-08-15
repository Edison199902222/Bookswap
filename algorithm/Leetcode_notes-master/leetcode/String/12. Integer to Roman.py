'''
用两个list 去代表 values 跟字符
然后遍历一遍 如果num 大于现在的value的话 那么就添加进去  并且num会减少 要用while
为什么要用while呢 因为会有情况 比如3 我们需要iii
'''


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        result = ""
        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                result += symbol[i]
        return result
