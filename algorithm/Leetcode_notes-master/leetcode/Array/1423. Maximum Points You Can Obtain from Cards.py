class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k >= len(cardPoints):
            return sum(cardPoints)
        sums = sum(cardPoints)
        presum = []
        presum.append(cardPoints[0])
        res = 0
        l = len(cardPoints)
        prefix_sum = cardPoints[0]
        for i in range(1, l):
            prefix_sum += cardPoints[i]
            presum.append(prefix_sum)
        for i in range(k + 1):
            if i == 0:
                res = max(res, sums - presum[i + l - k - 1])
                print(res)
            else:
                res = max(res, sums - (presum[i + l - k - 1] - presum[i - 1]))

        return res
'''
看到数组中 留下来的分数 是最大的 我们可以转化成
每一次 我们删除 l - k 个元素 
因为 只能从头部 或者 尾部 拿元素 也就是说 删除的元素 是连续的
那么 我们可以从数组的头遍历到尾部 对于每一个index 来说 我们删除 index 到 index + k 个元素
因为计算方便 所以 我们可以选择 用一个 prefix sum  的数组 来进行遍历
创建一个prefix sum的数组 每一个index 代表的是 包括自己index 上的元素 加上前面所有的元素的和
这样 我们就可以遍历 prefix sum  数组 分为两种情况
第一种情况 如果 index 等于 0  也就是删掉 我们前l - k 个元素时， 我们只需要用总的sums 减去 当前index 加上 我们要删去的几个元素 l -k 再 - 1 就是前要删去元素的和了
第二种情况 就是 我们需要删去某一段和 前面也有元素 但我们不需要删除， 那么就用上 总的sums 减去 （前l - k 个元素的和 再减去 i - 1 元素的和）就可以了

'''