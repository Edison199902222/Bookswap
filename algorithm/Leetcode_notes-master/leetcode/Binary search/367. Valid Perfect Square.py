class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 0
        right = num
        while left + 1 < right:
            mid = left + (right - left)/2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                right = mid
            elif mid * mid < num:
                left = mid
        if left * left == num:
            return left
        elif right * right == num:
            return right
        else:
            return False