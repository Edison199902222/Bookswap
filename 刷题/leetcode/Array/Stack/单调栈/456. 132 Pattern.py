class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        third = float("-inf") # 第三个值
        stack = [] # 储存的都是大于third 的值，维持递减的stack
        # 从后遍历数组， 先把第一个值放进stack中，如果出现有大于stack top的值，那么我们就更新third
        for i in range(len(nums) - 1, - 1, - 1):
            # third初始化是最小值，如果有值小于third，说明third已经被更新了，并且stack中有大于third的值，三个数已经找到
            if nums[i] < third:
                return True
            else:
                # 因为从后往前遍历，index 是递减的，如果发现有值 大于我们的stack 的top
                # 说明 我们j 跟 third 可以更新，把stack top的值作为我们third， top 的index 肯定是大于当前值的
                while stack and nums[i] > stack[-1]:
                    third = stack.pop()
                stack.append(nums[i])
        return False