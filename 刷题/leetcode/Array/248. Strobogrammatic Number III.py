class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        self.result = 0
        for i in range(len(low), len(high) + 1):
            for d in ["", "0", "1", "8"]:
                self.dfs(low, high, i, d)
        return self.result

    def dfs(self, low, high, length, path):
        if len(path) > length:
            return
        if len(path) == length:
            if path[0] == "0" and len(path) != 1:
                return
            elif int(low) <= int(path) <= int(high):
                self.result += 1
            return
        for d in ["00", "69", "88", "96", "11"]:
            self.dfs(low, high, length, d[0] + path + d[1])
'''
我们使用dfs
base case 如果当前组成的path 长度超出了我们的要求
我们就 return
如果 path 等于我们要求的长度
我们还需要检查 长度如果超过1的话 第一位不能为0 
如果 path大小 正好在我们要求的范围内的话 res 加1

不然的话 我们就继续 dfs搜索， 每次加上 两个数字， 头和尾
'''


class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        self.dic = {"1": "1", "0": "0", "6": "9", "8": "8", "9": "6"}
        self.result = 0
        # 通过 low 和 high 限制长度
        for i in range(len(low), len(high) + 1):
            # 最后结果是 i 这么长的number
            path = [0 for j in range(i)]
            self.dfs(0, path, low, high)
        return self.result

    def dfs(self, index, path, low, high):
        left = index
        right = len(path) - index - 1
        # 如果left 大于right，表示无更多数字可以填上
        if left > right:
            # 结果需要大于等于low 和 小于等于 high
            if int(low) <= int("".join(path[:])) <= int(high):
                self.result += 1
            return
            # 如果相等，有一位是空缺的，只能选择 0 1 8， 其他不能选
        elif left == right:
            for i in ["0", "1", "8"]:
                path[left] = i
                self.dfs(index + 1, path, low, high)
        else:
            # 两位以上是空着的话，可以选择 0 1 8 9 6
            for i in ["0", "1", "8", "9", "6"]:
                # 首位不能是0，首位的选择跳过0
                if index == 0 and i == "0":
                    continue
                path[left] = i
                path[right] = self.dic[i]
                self.dfs(index + 1, path, low, high)
        return