'''
用位运算才是最好解
其实 意思是
n&1 意思是 看现在这个位置上的 次方数是不是奇数 如果是奇数的话 就需要用pow乘
如果不是的话 只要自己乘自己就行
'''


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if  n < 0:
            x = 1/x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow*=x
            x*=x
            n>>=1
        return pow
