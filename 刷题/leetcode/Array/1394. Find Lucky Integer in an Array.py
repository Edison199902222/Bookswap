import collections


class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        lucky_number = -1
        dic = collections.Counter(arr)
        for key, value in dic.items():
            if key == value:
                lucky_number = max(lucky_number, key)
        return lucky_number