class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # 先找出所有不重复的点，并且统计各个点出现了几次， 因为重复的点也会作为result 算上
        counter = collections.Counter()
        for x, y in points:
            counter[(x, y)] += 1
        no_repeat_point = list(counter.keys())
        n = len(no_repeat_point)
        if n == 1:
            return counter[(points[0][0], points[0][1])]
        # 枚举点，记录每一个点跟当前点的斜率，斜率相同自然是一根线上的，我们要找的是斜率数量最多的
        # 用最大公约数记录斜率，因为除数精度不准确
        result = 0
        for i in range(n - 1):
            # 记录slop数量
            # 当前点
            x1, y1 = no_repeat_point[i][0], no_repeat_point[i][1]
            slop = collections.defaultdict(int)
            for j in range(i + 1, n):
                # 第二个点 求斜率
                x2, y2 = no_repeat_point[j][0], no_repeat_point[j][1]
                dy, dx = y2 - y1, x2 - x1
                # 求出 最大公约数， 因为除法不够精确
                g = self.gcd(dy, dx)
                if g != 0:
                    dy = dy // g
                    dx = dx // g
                # 查找有几个当前这样的点，并且加到slop
                slop[(dy, dx)] += counter[(x2, y2)]
            result = max(result, counter[(x1, y1)] + max(slop.values()))
        return result

    def gcd(self, x, y):
        if y == 0:
            return x
        return self.gcd(y, x % y)