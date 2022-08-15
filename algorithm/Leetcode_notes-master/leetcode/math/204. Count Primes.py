'''
先建立一个list
初始化每个为 None
然后 初始值第一个跟第二个是false 因为0 和 1 不是质数
然后遍历列表 如果为None的话 那么我们就展开 找到它的乘积 设置为false
'''


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 任何大于1的自然数，要么本身是质数，要么可以分解为几个质数之积，且这种分解是唯一的
        if n <= 2:
            return 0
        is_prime = [True for i in range(n + 1)]
        is_prime[0] = False
        is_prime[1] = False
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    print(i, p)
                    is_prime[i] = False
            p += 1

        result = []
        for i in range(2, n):
            if is_prime[i]:
                result.append(i)
        return len(result)