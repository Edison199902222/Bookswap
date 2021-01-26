class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        result = 0
        nums.sort()
        heap = []
        # 用扫描线
        count = [0] * (len(nums))
        for x, y in requests:
            count[x] += 1
            if y + 1 < len(nums):
                count[y + 1] -= 1
        operation = [0 for i in range(len(nums))]
        carry = 0
        for i in range(len(operation)):
            carry += count[i]
            operation[i] += carry

        for i in range(len(operation)):
            heapq.heappush(heap, (-operation[i], i))
        index = len(nums) - 1
        while heap:
            f, number = heapq.heappop(heap)
            result += nums[index] * (-f)
            index -= 1
        return result % (10 ** 9 + 7)


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        result = 0
        nums.sort()
        heap = []
        # 用扫描线, 找到每个index 的次数, 370 range addition
        count = [0] * (len(nums))
        for x, y in requests:
            count[x] += 1
            if y + 1 < len(nums):
                count[y + 1] -= 1
        operation = [0 for i in range(len(nums))]
        # 求出来后，排序一下
        carry = 0
        for i in range(len(operation)):
            carry += count[i]
            operation[i] += carry
        # 然后次数少的分配数字小的，次数多的分配数字大的
        operation.sort()
        result = 0
        for i in range(len(nums)):
            result += nums[i] * operation[i]
        return result % (10 ** 9 + 7)
