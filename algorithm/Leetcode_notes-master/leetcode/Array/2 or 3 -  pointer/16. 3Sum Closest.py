
'''
先把 列表 进行排序 这样好方便 等下进行缩小范围 操作
然后先把res初始化 任意列表中三个元素
然后进行遍历 遍历过程中 每次取一个 i+1 作为 头指针 end 是最后一个元素 作为尾指针
然后把当前数 与头指针 与 尾指针 指向的数加起来 如果这个数比我们的target大 那么我们end 就要缩小 因为列表从小到大排列
如果比我们的target小 那我们start 就要扩大
最后再比较 我们这次的 这三个数相加起来 与target的差值 是不是比之前取得差值 小
如果小的话 那么我们就更新res
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = float("inf")
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sums = nums[i] + nums[left] + nums[right]
                if abs(sums - target) < abs(result - target):
                    result = sums
                if sums > target:
                    right -= 1
                elif sums <= target:
                    left += 1
        return result