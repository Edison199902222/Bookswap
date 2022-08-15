'''
枚举先
tow point同向双指针
先累加 一旦sums大于等于s了 先把这个length添加进res 并且跟之前的res比较
然后开始缩小范围 用while 在这个区间内不断去缩小length
我们需要不断把 left 往右边移动 因为这样才能使得总体减小
最后检查res是不是跟最大值相等 如果相等说明没有这个值存在
'''

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums or not s:return 0
        sums = 0
        left = 0
        res = float("inf")
        for i in range(len(nums)):
            sums += nums[i]
            while sums >= s:
                res = min(res,i - left +1)
                sums -= nums[left]
                left += 1
        if res == float("inf"):
            return 0
        else:
            return res
'''
其实可以看作，我们寻找一个在整个数组中 寻找一个left，与right  这个left 与right之间的距离越小越好，使得left 到right的位置要大于等于s
所以我们用right 慢慢往窗口加东西，如果发现大于等于s了，我们就尝试移动右边指针

为什么每次移动right之后 不用初始化left呢？ 
因为假设 当前的left 到 right 刚好满足条件，我们移动了left 使得当前窗口不满足条件了， 
那么我们移动right，又使得当前窗口大于s了， 我们没有必要再初始化left 因为 在前一个窗口中，left 到 right已经是大于s得了，现在right 往右边移动了一个格子
那么肯定也是也是大于s， 并且对于left 之前的所有index 也是大于s的！！所以没有必要重新初始化！！窗口左边移动 会递减。
'''
if __name__ == '__main__':
    solution = Solution()
    print(solution.minSubArrayLen(7,[2,3,1,2,4,3]))