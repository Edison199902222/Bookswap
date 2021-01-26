class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        b = set(nums)
        a = set([i for i in range(1,length+1)])
        return list(a-b)