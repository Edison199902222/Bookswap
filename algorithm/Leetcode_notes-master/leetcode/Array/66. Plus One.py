'''
从后往前遍历 如果发现这一位的数字不是9 那么直接加1 并且return
如果发现是9 那么把这一位变成0 继续遍历
如果发现可以遍历完 说明全部数字变成0
那么我们需要 把第一位变成1 末尾加上一个0
例如 999
变成 000
100
1000
'''


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] +=1
                return digits
        digits[0] = 1
        digits.append(0)
        return digits