'''
 n - (n & -n)  效果为减去n的二进制上 最右边 为1 的
 比如 4 的二进制是100， 减去以后变成 000
 而且 减去右边的1 以后 肯定比原来的n小
 所以可以用迭代求解
 每一次的数 其实就是之前 n - (n & -n)的多少个1 加一个 就是当前数字多少个1 了
'''




class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        count = [0 for i in range(num+1)]
        for i in range(1,num+1):
            count[i] = count[i - (i & -i)]+1
        return count
