class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        m = len(mat)
        n = len(mat[0])
        presum = [[0] * (n + 1) for i in range(m + 1)]
        # 算出每个从 (0,0) 到 (i,j) 的面积和

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 计算左边
                presum[i][j] = presum[i][j - 1] + mat[i - 1][j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 计算上面
                presum[i][j] += presum[i - 1][j]
        left = 0
        right = min(m, n)
        # 查找长度，以mid 为边的正方形，sum有没有小于等于target 的
        while left + 1 < right:
            mid = (left + right) // 2
            if self.valid(presum, threshold, mid, m, n):
                left = mid
            else:
                right = mid

        if self.valid(presum, threshold, right, m, n):
            return right
        if self.valid(presum, threshold, left, m, n):
            return left
        return 0

    def valid(self, presum, target, mid, m, n):
        sums = float("inf")
        # 把mid 作为边长开始检查，找出每一个边长为mid 的正方形最小面积数
        # 为什么不用mid + 1，因为mid 在 m + 1的数组就刚好是长度为mid 的index
        for i in range(mid, m + 1):
            for j in range(mid, n + 1):
                # 面积数等于，当前i j sum 和，减去左边 跟上面 再加上 左边 跟上面重复的部分
                sums = min(sums, presum[i][j] - presum[i - mid][j] - presum[i][j - mid] + presum[i - mid][j - mid])

        if sums > target:
            return False
        return True

