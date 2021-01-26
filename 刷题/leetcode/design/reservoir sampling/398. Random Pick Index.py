class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        nums = None
        count = 0
        for i in range(len(self.nums)):
            if self.nums[i] != target:
                continue
            # 如果当前 number 跟target 相等
            else:
                # 如果第一次遇到target，直接指向当前index，count += 1
                if nums == None:
                    nums = i
                    count = 1
                # 如果不是第一次遇到target，那么跟当前count 随机，随机的数跟当前count 相等，则替换
                # 如果当前count为1，说明之前遇到一次target，现在有两个相同的target，从0 和 1 之间随机选取一个数
                # 概率是1/2，每遇到一个target 都跟当前随机一次，概率是1/n
                else:
                    if random.randint(0, count) == count:
                        nums = i
                    count += 1
        return nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)