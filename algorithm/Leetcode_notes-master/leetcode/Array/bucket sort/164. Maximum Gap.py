class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        min_value, max_value = min(nums), max(nums)
        # 桶长度 = 区间总长度 / 区间总个数 = (max - min) / (nums.length - 1)
        bucket_size = max(1, (max_value - min_value) // len(nums) - 1)
        # 确定桶的个数
        # 最后 加1 是因为区间其实是左闭右开 [  )， 最大值没有包括进去
        # // 还是举上面的例子，[2,4,6,8], 桶的长度 = (8 - 2) / (4 - 1) = 2
        #  桶的个数 = (8 - 2) / 2 = 3, 如果当前元素是 8 的话 (8 - 2) / 2 = 3，对应到 3 号桶
        #  如果当前元素是 2 的话 (2 - 2) / 2 = 0，对应到 0 号桶, 说明我们需要四个桶子 而不是三个桶子
        bucket_number = (max_value - min_value) // bucket_size + 1

        bucket_min, bucket_max = [float("inf")] * bucket_number, [0] * bucket_number
        for num in nums:
            # 计算落在哪个桶子上
            index = (num - min_value) // bucket_size
            bucket_min[index] = min(bucket_min[index], num)
            bucket_max[index] = max(bucket_max[index], num)
        result = 0
        last_index = 0
        for i in range(1, bucket_number):
            if bucket_min[last_index] == float("inf") or bucket_max[i] == 0:
                continue
            result = max(result, bucket_min[i] - bucket_max[last_index])
            last_index = i
        return result


