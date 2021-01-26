class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        left = max(nums)
        right = sum(nums)
        while left + 1 < right:
            # 假设largest sum
            mid = (left + right) // 2
            # 如果以mid来划分array， 能分成小于等于m段的话， 我们选的mid太大了, 我们要缩小数组能接受的和
            # 如果满打满算情况下 最少需要 n 个区间来split array， n 小于等于m个，n 是可以 变成m个的
            # 需要把 n 中的元素 拿出来几个 单独成为几个区间，
            if self.caculate(nums, mid) <= m:
                right = mid
            # 大于m段， 需要把mid 调大 让 mid 小一点
            # 如果n 大于m， 在满打满算的情况下， 最少需要n个区间，无法形成m个区间， 所以把mid调高， 使得n 变小
            else:
                left = mid
        # 先检查left 因为题目需要最小能使数组 分成 m 段的 value
        if self.caculate(nums, left) <= m:
            return left
        return right

    # 统计和小于等于给定target的连续数组个数
    # 这里算的是满打满算的情况， 会在给定value 下 求出最少需要 m 个区间
    def caculate(self, nums, largest_value):
        # 假设largest_value， 检查array能分成多少段
        count = 0
        sums = 0
        for num in nums:
            sums += num
            if sums > largest_value:
                count += 1
                sums = num
        # 注意， 最后的值如果没有大于larget value，还是多分一段
        # [7,2,5,10,8] larget = 21， 7 2 5 分一段， 10 + 8 = 18 不大于large value， 但是还需要多分一段
        # 最后count 需要加1
        if sums <= largest_value:
            count += 1
        return count

