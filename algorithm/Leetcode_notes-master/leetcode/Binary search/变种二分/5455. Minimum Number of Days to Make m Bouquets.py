class Solution(object):
    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return - 1
        left = min(bloomDay)
        right = max(bloomDay)
        while left + 1 < right:
            mid = (left + right) // 2
            # 大于等于m， 调小天数， 因为想找 Minimum Number of Days
            if self.caculate(bloomDay, mid, k) >= m:
                right = mid
            else:
                left = mid
        if self.caculate(bloomDay, left, k) >= m:
            return left
        elif self.caculate(bloomDay, right, k) >= m:
            return right
        return -1

    # 算以day为盛开的天，数组里有多少花会形成bouquet
    # 用这个算法 可以算 一个数组内 有多少连续的子数组 小于等于给定值
    def caculate(self, nums, day, k):
        result = 0
        count = 0
        for right in range(len(nums)):
            if nums[right] <= day:
                count += 1
                if count == k:
                    result += 1
                    count = 0
            else:
                count = 0
        return result
