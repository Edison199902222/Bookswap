class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        N = len(target)
        M = 1 << N
        # dp[i] 每个i 表示一个二进制，比如 001 表示 第一位的字母已经找到的minimum number of stickers
        # 需要找到 m 的二进制 全是1 的情况
        dp = [float("inf")] * M
        # 初始化， 000 啥都没找到的情况 肯定是用了 0个
        dp[0] = 0
        s = collections.Counter(target)
        # 首先修改已有的贴纸字符串，把和目标字符串不相交的部分删除。
        B = [collections.Counter(stick) & s for stick in stickers]
        # 接着对于修改后的数组，很显然有 "e" 总是劣于 "ea"，于是可以删除 "e" ，变成 ["th", "ea"], "thehat" 。
        check = set()
        for i in range(len(B)):
            for j in range(i + 1, len(B)):
                if B[i] | B[j] == B[i]:
                    check.add(j)
        A = []
        for i in range(len(B)):
            if i in check:
                continue
            A.append(B[i])

        for i in range(M):
            # 当前没有的状态 跳过
            if dp[i] == float("inf"):
                continue
            # 对于A的每一个单词的每一个字母，尝试在target 中寻找以当前状态 + 当前字母 可以得到的状态进行更新
            for char in A:
                # 当前的状态
                status = i
                new_count = char.copy()
                # 遍历taregt 的长度， 也就是看target 中哪一个字符 在当前word中有
                for j in range(N):
                    # 如果当前状态的第j位是空， 并且第j 位刚好是 k的话
                    # 说明现在可以提供第j个
                    if (status >> j) & 1 == 0 and new_count[target[j]] > 0:
                        # 跟之前的status 取交集， 说明第j个已经取到了
                        status |= 1 << j
                        new_count[target[j]] -= 1
                # 如果不等于原状态， 进行更新
                if i != status:
                    dp[status] = min(dp[status], dp[i] + 1)

        return dp[M - 1] if dp[M - 1] != float("inf") else - 1

