class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(1 << n):
            res.append((i >> 1) ^ i)
        return res
'''
于是只需遍历从 0 到 2^n - 1 的所有整数 i，使用公式将其转换为格雷码，添加到 List 中即可。
公式 i ^(i >> 1))
'''