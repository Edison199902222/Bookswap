class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1:
            return []
        self.result = []
        factor = self.find_factor(n)
        if not factor:
            return []
        self.dfs(0, factor, [], n)
        return self.result

    def find_factor(self, n):
        factor = []
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                factor.append(i)
                if i != n // i:
                    factor.append(n // i)
        factor.sort()
        return factor

    def dfs(self, index, factor, path, n):
        if n == 1:
            self.result.append(path)
            return
        if n < factor[index]:
            return
        for i in range(index, len(factor)):
            if n % factor[i] == 0:
                self.dfs(i, factor, path + [factor[i]], n // factor[i])

'''
用dfs ➕减去枝
首先 我们减枝
我们创建一个函数 find factor  去挑选出 所有合适的factor， 技巧就是下限是2 到 开根号 + 1的范围， 每一次不仅添加自己 并且还要添加 n // i
这样我们就可以得到所有合适的factor
然后我们用这个factor 去dfs
base case 如果n == 1 的话 说明我们找到了一个乘起来等于n的path
如果 n 小于我们 factor中的最小值的话 那么肯定不行，直接return
index 从0 开始 
我们去尝试从index 到 len（factor）
如果n 可以被factor中的元素 除尽的话， 我们就把它dfs下去
如果不行的话 就跳过，为什么dfs 每一次index是 i呢， 防止重复使用

'''


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        factor = self.find_factor(n)
        self.result = []
        self.dfs(factor, n, 1, [], 0)
        return self.result

    def find_factor(self, n):
        result = []
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                result.append(i)
                if i != n // i:
                    result.append(n // i)
        result.sort()
        return result

    def dfs(self, factor, n, sums, path, index):
        if n == 1:
            return
        if sums > n:
            return
        if sums == n:
            self.result.append(path)
            return
        for i in range(index, len(factor)):
            if n % factor[i] == 0:
                self.dfs(factor, n, sums * factor[i], path + [factor[i]], i)
        return