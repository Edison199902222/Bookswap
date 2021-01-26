class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = min(nums)
        right = max(nums)
        while left + 1e-6 < right:
            mid = (left + right) / 2
            if self.decide(nums, mid, k):
                left = mid
            else:
                right = mid
        return left

    def decide(self, nums, average, k):
        prefix_sum = [0]
        min_value = float("inf")
        for i in range(len(nums)):
            prefix_sum.append(nums[i] - average + prefix_sum[-1])  # 我们想让数组中所有的数字减去average再加起来，那么我们对于每个数字减去average再加上之前数字减去average的和 是一样的道理
            if i < k - 1:  # 我们想保证至少取到k个数时 才开始进行判断
                continue
            min_value = min(min_value, prefix_sum[
                i + 1 - k])  # 保证最小从index 0 ～ i + 1 - k 之间 取一个最小值，因为我们想要做到minvalue尽可能小，这样我们用当前的累加和 减去之前最小数才可以直到 会不会有一段大于等于0
            if prefix_sum[-1] - min_value > 0:
                return True
        return False
'''
二分法变种
我们通过二分法 不断尝试 平均值是多少
首先 平均值肯定介于 数组的最小值 到 最大值之间
然后 因为我们的精确度是要求在 10^-6 所以我们需要 left + 10^-6 < right 维持两个指针在 10^-6之间

然后 我们创建一个子函数 我们去判断，如果以当前的值 作为我们最大average 行不行
我们发现的技巧就是， 如果一个值是 一个nums 的大于等于最大平均值的话，那么nums中 每一个元素 减去 这个最大平均值 加起来 绝对是小于等于0的
所以 子函数中，我们创建一个prefix sum 数组，里面放着每一个元素 减去 我们猜想的最大平均值 再加上之前的元素减去最大平均值的累加和

用min value 去 指向 当前subarray  的最小值
比如 累加和是【0，-2，-3，-5，5】数组是【1，2，3，4】 k = 2 当我们遍历到数组的第三个元素 3 也就是i = 2 时，j = 1首先数组满足了 k = 2 的信息 
然后 我们就检查 从 index  j 之前， 最小的值是多少，因为我们想要做到minvalue尽可能小，这样我们用当前的累加和减去之前最小数， 才能知道 这一段数组中是不是存在大于0的累加和
那么我们可以检查到， 最小值是 -2 这种情况是由第一个元素 1 减去 平均值得到的，因为我们的可以大于等于k， 所以我们才需要追踪最小值

prefix sum 初始化时要放入0 是因为当现在数组刚好遍历到i，i = k -1时，说明我们刚好满足数组中有k个数，也就是0 ～ i，但是之前并没有任何数字，也就是最小值为0 

创建完这些以后，我们遍历数组，每一次遇到一个元素 我们用它减去我们设想的最大平均值再加上之前的累计和，如果遍历还没超过k - 1 时， 那么就跳过
如果满足 我们有k个元素了，那么我们就更新最小值，并且检查 如果当前的累计和 减去最小值 大于0 说明我们现在有一段subarray 的累计和 是大于0 了 
这也就说明 我们所选取的平均值是不对的，我们选取的平均值小了一些
那么我们移动左指针 = mid
遍历完 发现没有subarray 的累计和大于0， 说明我们选取的平均值 大于等于最大平均值，那么我们移动右边指针 看看能不能选取更小的一个平均值
最后 我们可以return left 也可以return right 
'''