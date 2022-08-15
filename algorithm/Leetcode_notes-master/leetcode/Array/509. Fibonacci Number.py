class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 1:
            return N
        res = [0 for i in range(N+1)]
        res[0] = 0
        res[1] = 1
        for i in range(2,N+1):
            res[i] = res[i-1] + res[i-2]
        return res[N]