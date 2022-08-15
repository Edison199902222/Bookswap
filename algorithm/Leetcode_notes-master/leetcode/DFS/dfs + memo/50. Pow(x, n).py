class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        self.memo = {}
        if n < 0:
            return 1 / self.dfs(x, - n)
        return self.dfs(x, n)

    def dfs(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n in self.memo:
            return self.memo[n]
        compolent = n // 2
        result = self.dfs(x, n // 2) * self.dfs(x, n - (compolent))
        self.memo[n] = result
        return result

'''
可以用dfs + memo 解
base case 就是 n == 0的话直接return 1
n == 1 的话 直接return x 本身
然后每次算出 n // 2  跟 n - n//2， 比如 n =3， 我就会有1 跟 2， 然后 1 * 2 就是当前n = 3的答案
放进memo中
'''