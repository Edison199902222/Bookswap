class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        for row in grid:
            left = 0
            right = len(row)
            while left + 1 < right:
                mid = (left + right) // 2
                if row[mid] >= 0:
                    left = mid
                else:
                    right = mid
            if row[left] < 0:
                result += len(row) - left
            else:
                result += len(row) - right
        return result
