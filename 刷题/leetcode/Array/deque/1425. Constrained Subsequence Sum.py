import collections
class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        deque = collections.deque()
        dp = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            if deque:
                dp[i] = deque[0] + nums[i]
            else:
                dp[i] = nums[i]
            while deque and dp[i] >= deque[-1]:
                deque.pop()  # make sure the frist place of deque is max value
            if dp[i] > 0:
                deque.append(dp[i])  # we dont want to negetive value
            if i >= k and deque and deque[0] == dp[i - k]:  # deque must not be 0
                deque.popleft()
        return max(dp)


'''
创建一个 deque  跟 dp数组 
deque 维护一个从大到小递减的 最大和 数组， deque的首位元素是最大和
dp[i]表示从数组 第i个位置  的最大sum 和

那么我们遍历数组 如果deque中没有东西的话 说明之前没有任何元素 或者说之前有元素但是最大和是负数，所以我们重新开始， 所以当前的最大和就是自己本身
如果前面有元素， 说明之前有正数最大和 那么我们就拿deque中最大值 加上自己的值 就是当前状态下 包括自己本身元素的 最大和了

即算完成后， dp[i]就是我们当前这个位置的最大和了， 我们把当前元素最大和 与 deque中 最后一位元素进行比较， 如果比它大 就把最后一位元素踢出来 不断重复
直到是一个从大到小的order
然后我们再判断 当前最大和是不是大于0，如果不是大于0 的话， 我们并不想要一个负数加入我们的deque，因为负数的值会拖累后面的值
最后我们检查 为下一个循环检查deque的最大值 还是不是合法， 也就是 是不是没有超过i - k个距离
'''