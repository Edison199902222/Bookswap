class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        x_max = float("-inf")
        x_min = float("inf")
        all_point = set()
        # 记录 x 的最大值，和 x 的最小值
        # 把所有点放进set中，把重复的点看成一个点
        for i in range(len(points)):
            x_max = max(x_max, points[i][0])
            x_min = min(x_min, points[i][0])
            all_point.add((points[i][0], points[i][1]))
        # 对称线 是由 x的最大值 加上x的最小值 / 2 得到的
        # 得到最大值后，我们可以知道 x y 分别为 对称线的两个点，对称线的值为z
        # （x + y）/ 2 = z， 那么 x = 2 * z - y
        # 根据公式得出，我们想要知道任何一点 经过 对称线对称的点，只需要对称线 乘2 减去 当前x
        reflect_line = (x_max + x_min) / 2
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            reflect_x = reflect_line * 2 - x
            if (reflect_x, y) not in all_point:
                return False
        return True
'''
首先我们要得到对称线在哪
对称线 会等于 两个点对称点的x 的总和 比如 (-2,0) (2,0)他们的对称线就是 2 + （-2） 等于 0
他们 x = 0 对称
我们需要找到两个对称点 去确定 对称线
所以 我们从数组中找到x的最大值跟x的最小值， 如果有对称线的话，这两个点肯定是对称点
然后我们遍历数组 找到x的最大值跟最小值 同时把所有点 放进set中 需要set的原因就是 数组中有可能有重复点 但是我们把这些点都当成一个点
然后再次遍历数组
对于每一个点的x， 我们用对称线的x 减去它 这样就求出它的对称的x的值 然后看存不存在于set之中

'''