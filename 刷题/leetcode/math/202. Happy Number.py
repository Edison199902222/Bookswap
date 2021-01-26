'''
用set
每次先把n加进去
然后拆开 相乘 等于新的n
终止条件是 如果n = 1 或者 一直重复i 个数字时
我们就判断n是不是1
'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cycle = set()
        while n!=1 and n not in cycle:
            cycle.add(n)
            n = sum((int(i)*int(i) for i in str(n)))

        return n == 1
if __name__ == "__main__":
    solution = Solution()
    print(solution.isHappy(19))