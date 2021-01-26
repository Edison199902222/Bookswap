class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        # 看到subarray， 就往presum 去想
        # 因为每次的prefix sum 都是带上当前元素的，所以如果当前presum - target  = x 在dic中
        # result 就直接加上 x出现的次数，因为必须带上当前元素进行presum 所以跟前面的肯定不会有一摸一样的array
        prefix = 0
        result  = 0
        dic = collections.defaultdict(int)
        dic[0] = 1
        for i in range(len(A)):
            num = A[i]
            prefix += num
            if prefix - S in dic:
                result += dic[prefix - S]
            dic[prefix] += 1
        return result