class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.result = []
        self.dfs(s, [], 0)
        return self.result

    def dfs(self, s, path, index):
        # base case
        if len(path) == 4 and index == len(s):
            self.result.append(".".join(path[:]))
            return
        # 如果不满足条件
        if len(path) == 4 or index == len(s):
            return
        # 每次选择抽一个，还是两个，还是三个
        for i in range(1, 4):
            # 如果index 超出范围
            if index + i > len(s):
                break
            # 如果第一个数是0， 那么之后的都不行
            if i > 1 and s[index] == "0":
                break
            substring = s[index : index + i]
            # 如果切出来的数，不满足条件，直接break，因为后面的也不会满足条件了
            if int(substring) < 0 or int(substring) > 255:
                break
            path.append(substring)
            self.dfs(s, path, index + i)
            path.pop()
        return