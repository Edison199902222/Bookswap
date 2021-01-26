'''
这道题 是一个变种的二分法
除法的含义其实就是 每次减去除数
那么 每一次 我们扩大除数 直到除数是小于 或者 等于被除数
同时 记录 扩大了多少次
最后 记录扩大了多少次 就可以知道 可以除几次
'''
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
            if abs(dividend) < abs(divisor):
                return 0
        a = abs(dividend)
        b = abs(divisor)
        sums = 0
        count = 0
        res = 0
        while a >= b:
            count = 1
            sums = b
            while sums + sums <= a:
                sums+=sums
                count+=count
            a-=sums
            res+=count
        if sign == -1:
            res = sign*res
        if res >= pow(2, 31) - 1 and sign == 1: return pow(2, 31) - 1
        if res >= pow(2, 31) and sign == -1: return -pow(2, 31)
        return res
if __name__ == '__main__':
    solution = Solution()
    a = -2147483648
    b = -1
    print(solution.divide(a,b))
