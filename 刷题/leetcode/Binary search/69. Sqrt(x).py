
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 1
        right = x
        while left + 1 < right:
            mid = (left + right) // 2
            if mid * mid > x:
                right = mid
            else:
                left = mid
        if right * right <= x:
            return right
        else:
            return left
if __name__ == '__main__':
    solution = Solution()
    print(solution.mySqrt(9))

