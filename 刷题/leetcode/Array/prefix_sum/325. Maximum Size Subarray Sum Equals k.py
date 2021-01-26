class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        '''
        we want to find a subarray which is equal to k
        so, we need find an array which is equal to x
        if prefix sum of the array which is eqaul to x - k
        there will exit a subarray within the array which is equal to x - (x - k) = k
        '''
        if not nums:
            return 0
        prefix = 0
        # if we find a array which is equal to k, it also need x - k, which is 0
        dic = {0:-1}
        result = 0
        for i in range(len(nums)):
            prefix += nums[i]
            if prefix - k in dic:
                result = max(result, i - dic[prefix - k])
            if prefix not in dic:
                dic[prefix] = i
        return result
'''
利用前缀和
记录数组的每一个前缀和 
如果发现前缀和中有一个子数组等于 当前sum - k的话
说明从 0 到现在 index的array中 含有一段子数组 等于k
'''