class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        left = 0
        # 当target很大时， array能形成最接近target的数， 就是 把array的值全部加起来
        # 想要使得array的值全部加起来， 必须使得寻找的数 大于等于array的最大值
        right = max(arr)
        while left + 1 < right:
            mid = (left + right) // 2
            if self.caculate(arr, mid) >= target:
                right = mid
            else:
                left = mid
        result1 = self.caculate(arr, left)
        result2 = self.caculate(arr, right)
        if abs(result1 - target) <= abs(result2 - target):
            return left
        return right

    def caculate(self, nums, value):
        count = 0
        for num in nums:
            if num > value:
                count += value
            else:
                count += num
        return count