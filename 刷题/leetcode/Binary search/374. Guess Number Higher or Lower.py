
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):
'''
为什么 是小于等于呢 因为这里的right 是n 这个n我们也想要取到

'''
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left,right = 1,n
        while left <= right:
            mid = (left + right)//2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                left = mid+1
            else:
                right = mid-1