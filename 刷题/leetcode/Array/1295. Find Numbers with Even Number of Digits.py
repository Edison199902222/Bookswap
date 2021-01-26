class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return 0
        count = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                count+=1
        return count