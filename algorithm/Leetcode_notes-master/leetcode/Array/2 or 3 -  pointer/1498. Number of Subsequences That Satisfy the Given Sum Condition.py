class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mod = 10 ** 9 + 7
        left = 0
        right = len(nums) - 1
        times = [1]
        # for i in range(1, len(nums) + 1):
        # times.append(times[-1] * 2)

        nums.sort()
        result = 0
        # 去等号是因为剩下一个数的时候也需要考虑
        while left <= right:
            sums = nums[left] + nums[right]
            # 满足条件，计算left 和 left 右边所有数的组合有几个
            # 限制： 必须带上left， 因为只有left 是必须选择
            # 因为只要存在right 并且满足条件了，又因为left 小于right， 所以left 单独的时候，也可以形成满足条件的
            if sums <= target:
                # result += times[right - left] % mod
                result += 1 << (right - left)
                left += 1
            else:
                right -= 1
        return result % mod
