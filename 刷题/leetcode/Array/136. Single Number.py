class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums:
            dic[i] = dic.get(i,0)+1
        for key,val in dic.items():
            if val == 1:
                return key
class Solution(object):
    def singleNumber(self, nums):
        res = 0
        for i in nums:
            res^=i
        return res