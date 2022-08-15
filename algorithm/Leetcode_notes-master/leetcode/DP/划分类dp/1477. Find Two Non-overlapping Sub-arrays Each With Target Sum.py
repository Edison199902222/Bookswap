class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)
        dic = {0:-1}
        # dp[i]表示前index i 个元素中满足target要求的子数组的最小长度
        dp = {-1 : float("inf")}
        pre = {0 : n}
        sums = pre_sums = 0
        #从左往右 用前缀和找到前index i 元素中满足target要求的子数组的最小长度
        for i in range(len(arr)):
            sums += arr[i]
            if sums - target in dic:
                dp[i] = min(dp[i - 1], i - dic[sums - target])
            else:
                dp[i] = dp[i - 1]
            dic[sums] = i
        result = float("inf")
        for i in range(n - 1, -1, -1):
            pre_sums += arr[i]
            if pre_sums - target in pre:
                result = min(result, dp[i - 1] + pre[pre_sums - target] - i )
            pre[pre_sums] = i
        return result if result != float("inf") else - 1

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        dic = {0:-1}
        # dp[i]表示前i个元素中满足target要求的子数组的最小长度
        dp = [float("inf")] * n
        pre = {0:n}
        sums = pre_sums = 0
        #从左往右 用前缀和找到前i哥元素中满足target要求的子数组的最小长度
        for i in range(len(arr)):
            sums += arr[i]
            if sums - target in dic:
                dp[i] = min(dp[i - 1], i - dic[sums - target])
            else:
                dp[i] = dp[i - 1]
            dic[sums] = i
        result = float("inf")
        for i in range(n - 1, 0, -1):
            pre_sums += arr[i]
            if pre_sums - target in pre:
                result = min(result, dp[i - 1] + pre[pre_sums - target] - i )
            pre[pre_sums] = i
        return result if result != float("inf") else - 1