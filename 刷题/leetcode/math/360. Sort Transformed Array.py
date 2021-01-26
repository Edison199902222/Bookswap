class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        n = len(nums)
        result = [None for i in range(n)]
        # 这是一个函数，当a 大于等于0的时候，nums 的两边的fx 呈现 递减状态  因为nums 也是排序好了的
        # 当a 小于0 的时候，nums 的两边的fx 呈现 递增状态
        # 所以利用双指针
        # 如果a 大于等于 0， idnex 从列表最后一位开始
        if a >= 0:
            index = n - 1
        # 小于0，index 从列表第一位开始
        else:
            index = 0
        # 指针从 列表两端往中间移动
        left = 0
        right = n - 1
        while left <= right:
            # 计算 列表两端的值
            left_value, right_value = self.caculate(a, b, c, nums[left]), self.caculate(a, b, c, nums[right])
            # 如果a 大于0，index 递减， 值也递减，所以 大的先放
            if a >= 0:
                if left_value >= right_value:
                    result[index] = left_value
                    left += 1
                else:
                    result[index] = right_value
                    right -= 1
                index -= 1
            # 如果a 小于0， index 递增，值也递增，小的先放
            else:
                if left_value >= right_value:
                    result[index] = right_value
                    right -= 1
                else:
                    result[index] = left_value
                    left += 1
                index += 1
        return result

    def caculate(self, a, b, c, x):
        return a * x * x + b * x + c