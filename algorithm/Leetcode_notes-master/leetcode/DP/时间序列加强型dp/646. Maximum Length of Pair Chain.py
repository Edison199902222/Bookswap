class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        # 因为要对每个start 找 匹配的end，所以sort start
        # sort了之后，我后面的end 一定要比 我现在的start要大，所以肯定不会漏掉任何一个 比我start 小的情况
        pairs.sort()
        dp = [1] * len(pairs)
        n = len(pairs)
        for i in range(n):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        # 创建一个数组
        nums = [float("inf")] * len(pairs)
        for start, end in pairs:
            # 对于每个start，在nums 找到一个end的是 第一个大于等于自己数的index
            index = bisect.bisect_left(nums, start)
            # 对index 进行 比较后，替换，把end 值较小的哪个 替换进去，因为end 值越小的，后面有可能start 接的越长
            nums[index] = min(nums[index], end)
        count = 0
        # nums 中不为最大值的数，就是max length 了
        for x in nums:
            if x != float("inf"):
                count += 1
        return count


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # 以end 排序
        # 因为 对于每一个chain，我们想要end越小越好，这样可以让后面的start 更有可能大于现在的end
        pairs = sorted(pairs, key=lambda x: x[1])
        prev_end = float("-inf")
        result = 0
        # 一开始把end 最小的放进来，如果后面没有任何一个start 大于最小的end，说明没有任何一个pair 是符合要求的
        # 如果有start 大于前面的end， 就放进来，因为已经保证了 end 从小到大去遍历
        for start, end in pairs:
            if start > prev_end:
                result += 1
                prev_end = end
        return result



