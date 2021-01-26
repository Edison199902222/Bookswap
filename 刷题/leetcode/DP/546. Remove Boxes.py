class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        length = len(boxes)
        dp = [[[0] * length for i in range(length)] for i in range(length)]
        return self.search(0, length - 1, 0, boxes, dp)

    def search(self, l, r, k, boxes, dp):
        if l > r:
            return 0
        if dp[l][r][k] != 0:
            return dp[l][r][k]
        while l < r and boxes[r] == boxes[r - 1]:
            k += 1
            r -= 1
        dp[l][r][k] = self.search(l, r - 1, 0, boxes, dp) + (k + 1) * (k + 1)
        for i in range(l, r):
            if boxes[i] == boxes[r]:
                dp[l][r][k] = max(dp[l][r][k],
                                  self.search(l, i, k + 1, boxes, dp) + self.search(i + 1, r - 1, 0, boxes, dp))

        return dp[l][r][k]
'''
dp[i][j][k] 意思是 我们从 index i ～ j 的最大分数 并且 后面有k个箱子是跟j 一个颜色的
所以 我们采用三维的dp
我们每一次 有两种情况
如果发现后面几个 是一样的， 那么我们的分数就是由 后面k个 数字的分数 加上 除掉k个数字的列表组成
第二种情况
分成两段处理 中间处理掉 把头和尾部相同的地方连起来处理
比如 23456222 那么我们先把3456作为一段处理，然后 前面的一个2 跟 后面三个2作为整体处理 为什么递归时self.search(l, i, k + 1, boxes, dp）k + 1， 
因为在之前操作时 我们已经算出 尾部有几个相同的元素 一旦发现前面的和后面的是相同的 我们只需要+ 1 就行了

'''