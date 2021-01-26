'''
双指针
直接交换
条件必须left 小于 right
因为当是偶数的时候 如果条件是 left！= right的话 right有可能小于left的 
'''
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

