
'''
理解题目意思：
h - index， 在 N个paper的数组中， h - index 的最大值就是N
比如【1，2，3】 我们有三个 paper， 他最大的h - index 就是3，不会超过paper的总数， 所以我们要寻找的h - index 范围是【0，N]
所以， 因为排序好了， 所以我们用二分检查
每次 检查 mid作为数组的第一个数 跟它右边所有数比较
比如【0，1，3，5，6】 mid index = 2， mid上面的值是3
我们算出mid右边包括mid有几个数， 也就是 n - mid = 3 个数， 然后我们想象以mid 为首个数字 与右边组成的数组
我们尝试用n - mid 作为h -index， 我们最小的数， 也就是mid上面的值 大于等于 n - mid（h -index） 的话
说明 这个h - index 是符合条件的，那就right = mid 尝试去寻找更大的h
反之， 我们向右边移动，寻找小的 h
'''


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        left = 0
        right = len(citations) - 1
        n = len(citations)
        # 每次都跟当前新数组的长度作为h-index 比较
        while left + 1 < right:
            mid = (left + right) // 2
            # mid 上面的值，作为新数组的最小的，如果最小的 都大于等于当前数组的length(n - mid)的话，说明整个都满足，n - mid 作为h -index
            if citations[mid] >= n - mid:
                right = mid
            # 不满足，往右边移动
            else:
                left = mid
        if citations[left] >= n - left:
            return n - left
        if citations[right] >= n - right:
            return n - right
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.hIndex([0,1]))