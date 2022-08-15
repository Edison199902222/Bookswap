
'''
先把matrix 统计出 每一行有多少个 1 然后排序
因为每一行中只有0或者1 只需sum 一行 就知道有几个1了
排序后 直接return 
'''
class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        S = [[sum(g),i] for i,g in enumerate(mat)]
        result = sorted(S)
        return [result[i][1] for i in range(k) ]
