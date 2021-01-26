'''
这道题意思是 求出时间
其实 就是 两个点之中 x y 减去后 得出的最大值 就是time
'''


class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        time = 0
        for i in range(len(points)-1):
            x_time = abs(points[i][0] - points[i+1][0])
            y_time = abs(points[i][1] - points[i+1][1])
            time += max(x_time,y_time)
        return time