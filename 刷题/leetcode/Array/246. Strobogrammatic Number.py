class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dic = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        left = 0
        right = len(num) - 1
        while left <= right:
            if num[left] not in dic or dic[num[left]] != num[right]:
                return False
            left += 1
            right -= 1
        return True
'''
用字典储存可以倒过来的数字
然后用双指针
遍历num 去判断
'''