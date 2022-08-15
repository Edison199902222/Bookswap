class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        res = 1
        for x in b:
            res = self.pow(res, 10) * self.pow(a, x) % 1337
        return res

    def pow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        compolent = n // 2
        result = (self.pow(x, compolent) % 1337) * (self.pow(x, (n - compolent)) % 1337)
        return result % 1337
'''
每次先算出个位数的power 然后 乘10 
比如 2^ 23， 先算出 2^20 * 2 ^ 3 
'''