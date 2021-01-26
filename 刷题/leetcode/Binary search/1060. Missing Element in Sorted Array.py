class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) < 2:
            return nums[0] + k
        # 整个数组一共有几个数
        whole_length = nums[-1] - nums[0] + 1
        # 计算中间一共有几个miss number
        whole_miss = whole_length - len(nums)
        # 如果中间缺少的数，少于要找的数的数量，那么直接返回 最后一个
        if whole_miss < k:
            return nums[-1] + (k - whole_miss)

        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            # 如果从left 到right 之间缺少的数，小于要找的k，往右边区间找
            # nums[mid] - nums[left] + 1 统计一共有几个数 从left 到right
            # (mid - left + 1) 统计left 到right  数组中有几个数
            # 相减就是 缺少了几个数
            miss_number = nums[mid] - nums[left] + 1 - (mid - left + 1)
            #
            if miss_number < k:
                left = mid
                k -= miss_number
            else:
                right = mid
        return nums[left] + k



