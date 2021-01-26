class ProductOfNumbers:
    # 利用前缀和
    def __init__(self):
        self.result = [1]

    def add(self, num: int) -> None:
        # 如果num 等于0， 重置result
        if num == 0:
            self.result = [1]
        else:
            self.result.append(self.result[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.result):
            return 0
        # 前缀和， 总的和 除以要计算区间前一个
        n = len(self.result)
        total = self.result[-1]
        before = self.result[-k - 1]
        return total // before

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)