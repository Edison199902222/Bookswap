class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {0: -1}
        prefix_sum = 0
        result = 0
        for i in range(len(nums)):
            if nums[i]:
                prefix_sum += nums[i]
            else:
                prefix_sum -= 1
            if prefix_sum in dic:
                result = max(result, i - dic[prefix_sum])
            else:
                dic[prefix_sum] = i
        return result

'''
我们如何知道 0 和 1 出现的次数 平衡了呢
我们把 0 当作 -1
建立一个pre sum 
意思是 从数组的起点 到 第i 个index 的和 
我们知道 如果 pre sum 等于0 的话 1 和 0 出现的次数就一样多了

但是 我们怎么知道 其他subarray 出现平衡的次数呢？
我们利用 pre sum来解决 假设 有 i < j 两个 index
两个index 的pre sum 相同 都是 1 
那么 我们只需要 用 j 的pre sum  减去 i 的pre sum 就会等于 1 - 1 = 0 
等于0 就说明1 和 0 出现的次数就一样多了
所以 我们用一个hash table 来记录每一次 第一次出现新的pre sum 的index
一旦 后面出现相同的pre sum， 我们就用j 的index 减去 i 的index 就是这个列表的长度了
代表着从i + 1 到j 这个区间的列表中 1 和 0 出现的次数相等

'''