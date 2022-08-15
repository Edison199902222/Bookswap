'''
以信封的宽度和高度排序，宽度小的在前，宽度一样，高度大的在前
然后 所有的高度构成一个数组，寻找此数组中的连续最长递增序列
'''


class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        #  # 其实是同时 找 w 和 h 的最长升序列
        # w相同时，按照h的逆序排序
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        n = len(envelopes)
        print(envelopes)
        result = [float("inf") for i in range(n)]
        size = 0
        # 因为 w 已经排序好，所以现在每一个都算是最长增序列的order
        # 只需要对h 找到最长升序列，把前面更新掉不代表要选择，因为更新掉前面的 不会影响size
        # 把最后一位更新掉，
        # 代表尝试选择当前的信封作为最后一个信封， 前面的信封不会收到影响 因为当前的w都大于前面的，并且h也大于除了最后一个的所有信封
        # 所以尝试把当前信封作为最后一个，还可以降低 最长增序列最后一位数的大小
        for i in range(len(envelopes)):
            index = self.binary_search(result, envelopes[i][1])
            result[index] = envelopes[i][1]
            size = max(size, index + 1)
        print(result)
        return size

    def binary_search(self, nums, value):
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] >= value:
                right = mid
            else:
                left = mid
        if nums[left] >= value:
            return left
        if nums[right] >= value:
            return right
        return len(nums)
'''
为什么要按照高度降序排序呢， 是因为 在width 相同时，我们想要高度越小越好， 因为对于每一个width 我们只需要一个height
我们想要找连续最长递增序列的话， 我们希望 在同width 时，height 越小， 组成的result 尽可能长
所以我们把高度大的 往前放， 这样的话， 如果高度小的也满足条件的话， 我们就会把高度大的替换掉，组成尽可能小的最长递增序列
'''
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes or not envelopes[0]:
            return 0
        result = []
        envelopes.sort(key = lambda x:(x[0], -x[1]))
        for envelope in envelopes:
            if len(result) == 0 or envelope[1] > result[-1]:
                result.append(envelope[1])
            else:
                index = bisect.bisect_left(result, envelope[1])
                result[index] = envelope[1]
        return len(result)

if __name__ == '__main__':
    envelopes = [[1,3],[3,5],[6,7],[6,8],[8,9],[9,5]]
    solution = Solution()
    res = solution.maxEnvelopes(envelopes)
    print(res)