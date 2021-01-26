class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        result = 1
        points = sorted(points, key=lambda x: x[1])
        end = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > end:
                result += 1
                end = points[i][1]
        return result
'''
又是一道区间 greedy 题
跟其他题不太一样的是，我们需要按照 end来排序 
我们按照 end 排序以后
我们初始化 result 为1 因为 我们待会会从数组的第二位开始遍历， 所以说我们至少射出一箭
把end 也设置成数组中第一位的end
然后 我们从第二个气球开始遍历
如果start 是 大于 我们之前气球的end 的话， 说明 这个气球 与之前的气球 没有 交集
那么我们需要多射一箭 才可以 所以result + 1 并且把 end 更新成当前气球的end
'''

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        result = len(points)
        points.sort()
        prev = points[0][1]
        for i in range(1, len(points)):
            # 如果小于前面的end的话，说明重合，那么不用多射一次，并且把end 调整，因为重合区间需要所有的气球重合的
            if points[i][0] <= prev:
                result -= 1
                prev = min(prev, points[i][1])
            else:
                prev = points[i][1]
        return result