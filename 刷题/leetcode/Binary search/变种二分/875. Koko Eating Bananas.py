class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        left = 1
        right = max(piles)
        while left + 1 < right:
            mid = (left + right) // 2
            if self.count(piles, mid) <= H:
                right = mid
            else:
                left = mid
        if self.count(piles, left) <= H:
            return left
        else:
            return right

    def count(self, piles, speed):
        result = 0
        for i in piles:
            if i % speed == 0:
                result += i // speed
            else:
                result += (i // speed) + 1
        return result
'''
与lintcode 183 题很像
我们用count function 去计算 以当前速度吃香蕉， 吃完piles 需要多少的小时
然后 我们用二分
范围是 从速度一小时一根 到 最大是 piles 的最大值
然后 每一次我们取mid
调用 count 函数 以mid的速度 算吃完这堆香蕉 需要多少小时， 如果小于等于 H 小时的话
因为题目要求 速度越小越好， 那么我们可以考虑调小速度 也就是 right = mid
如果大于H 小时的话， 那么我们就需要调快速度 满足题目要求
最后先检查 left的速度 因为速度越小越好
'''