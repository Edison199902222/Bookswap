
'''
dp

'''
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle: return 0
        res = triangle[-1]
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j],res[j+1]) + triangle[i][j]
        return res[0] # return 0 位置是因为这是一个三角形 从底下往上面推 最后只有两个去比较