'''
用两个指针
一个从头 一个从尾 因为是排序好的
每次 left + right 如果得出来的结果 小于 target
说明left 需要+ 1 得到更大的值
如果 大于right 说明需要更小的值 那么用right -= 1
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            temp_sum = numbers[left] + numbers[right]
            if temp_sum == target:
                return [left + 1, right + 1]
            elif temp_sum < target:
                left += 1
            else:
                right -= 1
