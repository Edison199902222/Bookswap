class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        self.result = []
        self.dfs(0, num, 0, 0, target, "")
        return self.result

    def dfs(self, index, num, cur_sum, prev_val, target, path):
        if cur_sum == target and index == len(num):
            self.result.append(path)
            return
        if index == len(num):
            return
        # 遍历每个nums， 因为根据不同长度，都可以组成数组作为当前值
        for j in range(index, len(num)):
            cur_val = int(num[index: j + 1])
            # 如果第一个是0的话，并且跟其他数组组成组合， 05， 06 这种是不合法的
            if j != index and num[index] == "0":
                break
            # 如果index 是第一个数的话，直接放进path
            if index == 0:
                self.dfs(j + 1, num, cur_val, cur_val, target, path + str(cur_val))
            # 不然的话， 有三种选择
            else:
                # 加号，直接加进去，并且把当前数 作为prev
                self.dfs(j + 1, num, cur_sum + cur_val, cur_val, target, path + "+" + str(cur_val))
                # - 号， 把 负cur val 作为 prev
                self.dfs(j + 1, num, cur_sum - cur_val, - cur_val, target, path + "-" + str(cur_val))
                # 一旦遇到乘号，那么当前sum - 上一个的val 可以得到 去掉前一个数的 值
                # 然后再加上，前一个数 跟 当前数相乘 就是结果
                self.dfs(j + 1, num, cur_sum - prev_val + prev_val * cur_val, prev_val * cur_val, target,
                         path + "*" + str(cur_val))
        return
if __name__ == "__main__":
    solution= Solution()
    print(solution.addOperators("41",5))
'''
dfs + backtracking

先用循环 因为对于每次来说 我们可以选择一位数 也可以选择两位数 或者 三位数 但是 如果以0开头的话 是不允许的
所以当前数字递归结束后 我们需要检查 当前数字是不是0 如果是0 那么我们循环中止 因为以0开头的数字 不允许
每次我们递归选择时 有四个选项 
如果index是0的话 那么我们不用加任何的计算符号
也可以选择 + - *

'''