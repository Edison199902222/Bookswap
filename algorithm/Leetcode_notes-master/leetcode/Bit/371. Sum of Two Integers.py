'''
https://darktiantian.github.io/371-Sum-of-Two-Integers-Python/
'''
class Solution(object):
    def getSum(self, a, b):
        MASK = 0xffffffff

        # in Python, every integer is associated with its two's complement and its sign.
        # However, doing bit operation "& mask" loses the track of sign.
        # Therefore, after the while loop, a is the two's complement of the final result as a 32-bit unsigned integer.
        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

        # a is negative if the first bit is 1
        if (a >> 31) & 1:
            return ~(a ^ MASK)
        else:
            return a