class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        self.oper = ["+", "-", "*", "/"]
        return self.dfs(nums)

    def dfs(self, nums):
        if not nums:
            return False
        if len(nums) == 1:
            return abs(nums[0] - 24) < 10 ** -6
        # 枚举两个，用四种方式 算结果，然后再放进里面，dfs 继续，直到剩下一个数字
        # 然后再判断 这个数字是不是跟24 相等
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                right = []
                for z in range(len(nums)):
                    if z != i and z != j:
                        right.append(nums[z])
                for k in self.oper:
                    if (k == "+" or k == "*") and i > j:
                        continue
                    if k == "/" and nums[j] == 0:
                        continue
                    right.append(self.operate(k, nums[i], nums[j]))
                    if self.dfs(right):
                        return True
                    right.pop()
        return False

    def operate(self, oper, x, y):
        if oper == "+":
            return x + y
        if oper == "-":
            return x - y
        if oper == "/":
            return x / y
        if oper == "*":
            return x * y




