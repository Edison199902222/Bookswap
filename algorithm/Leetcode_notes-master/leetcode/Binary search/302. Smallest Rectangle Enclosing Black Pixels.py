class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        if not image:
            return 0
        m = len(image) - 1
        n = len(image[0]) - 1
        left = self.check_left(image, 0, y)
        right = self.check_right(image, y, n)
        # 有了left 跟right 可以确定宽度
        top = self.check_top(image, 0, x)
        bottom = self.check_bottom(image, x, m)
        return (right - left + 1) * (bottom - top + 1)

    # 找到最左边的col上有1的，这样就找到最左边有1的边界
    # 二分的单调性是，如果此时mid的col 上没有1，mid 左边的都不会有1， 因为所有black pixel 是连接的
    def check_left(self, image, left, right):
        while left + 1 < right:
            mid = (left + right) // 2
            if self.check_col(image, mid):
                left = mid
            else:
                right = mid
        if self.check_col(image, left):
            return right
        return left

    # 找到最右边边的col上有1的，这样就找到最右边有1的边界， 确定宽度
    # 二分的单调性是，如果此时mid的row 上没有1，mid右边的都不会有1， 因为所有black pixel 是连接的
    def check_right(self, image, left, right):
        while left + 1 < right:
            mid = (left + right) // 2
            if self.check_col(image, mid):
                right = mid
            else:
                left = mid
        if self.check_col(image, right):
            return left
        return right

    def check_top(self, image, left, right):
        while left + 1 < right:
            mid = (left + right) // 2
            if self.check_row(image, mid):
                left = mid
            else:
                right = mid
        if self.check_row(image, left):
            return right
        return left

    # 二分的单调性是，如果此时mid的row 上没有1，mid 下面的row的都不会有1， 因为所有black pixel 是连接的
    def check_bottom(self, image, left, right):
        while left + 1 < right:
            mid = (left + right) // 2
            if self.check_row(image, mid):
                right = mid
            else:
                left = mid
        if self.check_row(image, right):
            return left
        return right

    def check_col(self, image, col):
        for i in range(len(image)):
            if image[i][col] == "1":
                return False
        return True

    def check_row(self, image, row):
        for i in range(len(image[0])):
            if image[row][i] == "1":
                return False
        return True


class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        list_points = []
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == "1":
                    list_points.append([i, j])

        max_x = 0
        max_y = 0
        min_x = float("inf")
        min_y = float("inf")
        for x, y in list_points:
            max_x = max(max_x, x)
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)
        return (max_x - min_x + 1) * (max_y - min_y + 1)