class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()
        # 间隔距离最小就是0
        left = 0
        # 间隔距离最大就是数组最大值
        right = max(position)
        while left + 1 < right:
            # 把mid
            mid = (left + right) // 2
            # 如果用 间隔距离 为 mid， 可以放超过m个球，说明间隔距离还可以尝试去增大，这样m 就会变小
            if self.helper(position, mid, m):
                left = mid
            # 如果间隔距离为mid 可以放 少于m个球的话，说明此时mid 太大了，间隔距离 mid 需要减少，让m 增大
            else:
                right = mid
        if self.helper(position, right, m):
            return right
        return left

    def helper(self, arr, mid, target):
        count = 0
        prev = -1
        for i in range(len(arr)):
            if (prev != -1 and arr[i] - prev >= mid) or i == 0:
                count += 1
                prev = arr[i]
        return count >= target






