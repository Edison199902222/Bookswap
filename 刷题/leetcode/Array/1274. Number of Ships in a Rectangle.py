# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Sea(object):
#    def hasShips(self, topRight, bottomLeft):
#        """
#        :type topRight: Point
#		 :type bottomLeft: Point
#        :rtype bool
#        """
#
# class Point(object):
#	def __init__(self, x, y):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea, topRight, bottomLeft):
        """
        :type sea: Sea
        :type topRight: Point
        :type bottomLeft: Point
        :rtype: integer
        """
        res = 0
        x1 = bottomLeft.x
        y1 = bottomLeft.y
        x2 = topRight.x
        y2 = topRight.y
        x3 = (x1 + x2) // 2
        y3 = (y1 + y2) // 2
        if x2 >= x1 and y2 >= y1 and Sea.hasShips(sea, topRight, bottomLeft):
            if x2 == x1 and y2 == y1:
                return 1
            res += self.countShips(sea, Point(x3, y3), Point(x1, y1), )
            res += self.countShips(sea, Point(x2, y3), Point(x3 + 1, y1))
            res += self.countShips(sea, Point(x3, y2), Point(x1, y3 + 1))
            res += self.countShips(sea, Point(x2, y2), Point(x3 + 1, y3 + 1))
        return res
'''
很明显，我们将二维平面划均分为四个区域，然后给自递归处理，计算每个区域的countShips，然后累积起来。

需要注意的几点：（1）划分区域的时候需要保证四块的边界不能重复。（
2）提前用hasShip来预判是否有船在区域内，如果没有，可以直接返回零。（3）边界条件是：当左上角与右下角重合时，返回的结果与hasShip的结果一致
'''