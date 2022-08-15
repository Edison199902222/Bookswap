class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.helper(n, n)

    def helper(self, n, m):
        if n == 0:
            return [""]
        if n == 1:
            return ["1", "0", "8"]
        temp = self.helper(n - 2, m)
        res = []
        for i in range(len(temp)):
            if n != m:
                res.append("0" + temp[i] + "0")
            res.append("1" + temp[i] + "1")
            res.append("6" + temp[i] + "9")
            res.append("8" + temp[i] + "8")
            res.append("9" + temp[i] + "6")
        return res
'''
两边往中间搜索
首先base case 如果n =1 那么只有 1 0 8 三个数字是了
如果等于0 那么只有空字符串
然后用temp 去指向所有  上一层 的组合（ n -2 是因为 每一层我们需要添加两个数字）
然后我们在这一层 遍历 上一层的所有组合
然后判断 这一层 是否 n ！= m 因为如果 n = m 的话 说明 现在添加的两个数字 是头跟尾了 那么不能添加 0 跟 0 
因为 0 跟 0 不能作为头尾
然后我们把所有组合 再加上 两个 符合的 number 重新添加进result中
最后return

'''


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        self.dic = {"1": "1", "0": "0", "6": "9", "8": "8", "9": "6"}
        self.result = []
        path = [0 for i in range(n)]
        self.dfs(0, path, n)
        return self.result

    def dfs(self, index, path, n):
        # 因为每次直接在path 里面更改， 不用回溯！！， 而不是append 跟pop
        left = index
        right = n - index - 1
        if left > right:
            self.result.append("".join(path[:]))
            return
        elif left == right:
            for i in ["1", "0", "8"]:
                path[left] = self.dic[i]
                self.dfs(index + 1, path, n)
        else:
            for i in ["0", "1", "8", "9", "6"]:
                if index == 0 and i == "0":
                    continue
                path[left] = i
                path[right] = self.dic[i]
                self.dfs(index + 1, path, n)
        return

