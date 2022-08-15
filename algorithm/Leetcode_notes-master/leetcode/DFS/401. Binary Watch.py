'''
这道题其实就是在算 在1024 中 转化为二进制 有多少个1 是等于我们num的
'''


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ans = []
        for i in range(12):
            for j in range(60):
                if (bin(i) + bin(j)).count("1") == num:
                    ans.append("%d:%02d" %(i,j))
        return ans