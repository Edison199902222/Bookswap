class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m = len(nums1)
        n = len(nums2)
        # 枚举 num1 最少能取几个数 ～ 最多可以取几个数
        # max(0, k - n)， 最少可以取0 个数 但取0 时， 需要看 nums2 中是否有k个数
        # 所以 最少可以取几个数 取决 k - n， 如果n 大于 k 会变成负数， 自然最少可以取 0 个
        # 如果n 小于k， 那么看k 比n 多几个数， 就是nums1 中最少要取几个数
        result = []
        for x in range(max(0, k - n), min(k, m) + 1):
            temp = self.merge(self.get_max(nums1, x), self.get_max(nums2, k - x))
            result = max(result, temp)
        return result

    # 从nums 中选择 target 个数， 保证order的情况下 ，能组成的最大值
    def get_max(self, nums, target):
        result = []
        n = len(nums)
        for i in range(n):
            # 如果当前result中的数量 加上还没有选择的数字的数量大于 t 的话，才能考虑pop的情况
            while result and len(result) + (n - i) > target and nums[i] > result[-1]:
                result.pop()
            if len(result) < target:
                result.append(nums[i])
        return result

    # 在两个数组中保证order 的情况下， 选出最大的数字组成array
    def merge(self, nums1, nums2):
        result = []
        # 取空为止
        while nums1 or nums2:
            # 保证相对顺序的情况下，只能取首位元素
            if nums1 > nums2:
                result.append(nums1[0])
                nums1 = nums1[1:]

            else:
                result.append(nums2[0])
                nums2 = nums2[1:]
        return result