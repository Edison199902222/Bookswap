class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        dic = {0:-1}
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum in dic:
                return dic[prefix_sum] + 1, i
            dic[prefix_sum] = i
        return -1, -1