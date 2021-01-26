'''

先把列表进行排序
遍历列表 一共有三个数字 目前遍历到的数字 i + 1作为头指针 列表最后一个作为尾指针 并且 如果发现当前数字 跟之前数字 是一样的话 要跳过 因为我们不需要重复的组合
然后开始进行缩小范围
把三个数字 加在一起  一个三种情况
第一种情况 如果 三个数字相加 刚好等于0 那么我们找对了 把三个数字 放进result 中
并且 我们还需要去除重复元素 如果发现头 或者 尾指针 的下一个元素 跟现在 头 尾指向的元素一样的话 那么我们就需要进行 跳过
最后 确保 头尾指针 指向的下一个元素是不一样的 那就各自指向下一个
第二种情况 如果加在一起 小于 0  说明我们需要更大一点的数字 因为是排序的 所以 start指针 往后移动
第三种情况如果加在一起 大于 0  说明我们需要更小一点的数字 因为是排序的 所以 end指针 往前移动
最后 return 结果
'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sums = nums[i] + nums[left] + nums[right]
                if sums == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:  # 去除重复
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sums > 0:
                    right -= 1
                else:
                    left += 1
        return result
