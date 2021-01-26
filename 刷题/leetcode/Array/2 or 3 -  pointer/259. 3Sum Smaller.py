class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = 0
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sums = nums[i] + nums[left] + nums[right]
                if sums < target:
                    result += (right - left)
                    left += 1
                else:
                    right -= 1
        return result
'''

跟之前的题不一样得是！！ 可以重复！！
先把数组排序
然后我们每一次 固定住左边
去尝试 第二个数字 跟第三个数
第二个数字就初始化 选择为 第一个数字的右边一个
第三个数字选择为数组为最后一个
因为数组已经排序了的， 所以 我们检查 如果当前sums 值超过了我们的target 我们就把right指针往左边移动 
如果 刚好没有超过， 那么说明 right 指针指向的数字 到 我们的mid 指针 指向的数字 的这些中间值都可以作为 我们的right指针来使用， 都可以满足我们target
结束后 我们继续 对数组下一个数组 设置为left 固定住 找另外两个值
'''