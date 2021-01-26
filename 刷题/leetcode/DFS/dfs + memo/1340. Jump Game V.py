class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        self.memo = {}
        self.result = float("-inf")
        for index in range(len(arr)):
            self.jump(index, arr, d)
        return self.result
    def jump(self,index, arr, d):
        if index in self.memo:
            return self.memo[index]
        result = 0
        for direction in [-1, 1]:
            for i in range(1, d + 1):
                j = index + i * direction
                if 0 <= j < len(arr) and arr[j] < arr[index]:
                    result = max(result, self.jump(j, arr, d))
                else:
                    break
        self.memo[index] = result + 1
        self.result = max(self.result, result + 1)
        return result + 1
'''
dfs + memo 求解
我们首先 创建一个memo 字典 记录 走过的index 与它对应的result
然后 我们遍历数组 假设从数组的每一个元素作为起点 开始jump
jump函数中 我们首先检查 如果index 在我们memo中 直接return
不然的话 我们开始 往左走 跟 往右走 得到新的index 记住 我们走的格数 不能超过d
并且每一次 新的index 要在数组范围之中 并且必须小于 当前index 的值 如果大于的话 直接break
然后 它的result 就会 等于 自身的最大值 或者 再次调用以j 为起点 jump 的结果
我们求出当前index 最大值之后 把它放进memo中 记录下来 
然后 返回我们的最大值 + 1 因为自身也算一个
'''