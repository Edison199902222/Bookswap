class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        nums.sort()
        dp = [1] * len(nums)
        prev = [-1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
        path = []
        max_val, last = max(dp), dp.index(max(dp))
        while last != -1:
            path.append(nums[last])
            last = prev[last]
        return path[::-1]
'''
# dp[i] 以dp[i]为最大值的子集的个数，此为核心数组，不会保存具体方案
# prev[i] 代表dp[i]的最优值从哪个j算过来的
初始化 dp 每个以自己为最大值子集的个数 肯定是至少是一个 因为光自己就是1
然后我们遍历数组 用i指向
然后用j 遍历 i之前的数字 
因为是已经排序好了 所以只需要判断 如果 目前的数（最大值） 可以被之前的数j 整除 并且 以j为最大值的子集 加上i 会大于我们当前以i为最大值的子集 个数的话
那么我们就更新dp
并且我们prev 也要更新成j，说明当前的dp最长子集 是由j转移得到的
最后我们 先求出dp中最大值 然后得到所在的index（因为这就是以index为最大值子集的个数）
把index 对应在nums中 加入进去， 然后我们再找到index 在prev中 所指向的数字 意思是 我们要知道 是从哪个j 转移来的

'''
if __name__ == "__main__":
    solution = Solution()
    print(solution.largestDivisibleSubset(solution.largestDivisibleSubset([1,2,3])))