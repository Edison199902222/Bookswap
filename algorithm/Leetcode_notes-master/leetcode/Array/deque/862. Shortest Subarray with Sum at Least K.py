import collections


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        deque = collections.deque()
        deque.append([0, 0])
        result = float("inf")
        sums = 0
        for index, value in enumerate(A):
            sums += value  # 计算当前累计和
            while deque and sums - deque[0][1] >= K:  # 计算是否当前array 用一段sub array 可以 大于等于k
                result = min(result, index + 1 - deque.popleft()[0])
            # 用了贪心的思想，每一个符合条件被pop的prefix subarray，就算后面有大subarray 符合条件，但是并不是最短的
            # 当sums 小于 等于deque 的最后一个元素，也pop， 这里也用了贪心
            while deque and sums <= deque[-1][1]:
                deque.pop()
            deque.append([index + 1, sums])
        return result if result != float("inf") else -1


'''
deque 递增
我们要寻找某个 subarray 的和 大于等于 k
所以 我们可以转化成， 把所有presum 求出来， 然后 index i < j
对于每一个index j ， 寻找 pre_sum[j] - pre_sum[i] >= k的话， 就说明我们存在一个sub array 的和 大于等于k
我们使用递增的deque 里面保存 length 跟 sub array的累计和
初始化deque时， 需要把0 放进去， 因为对于array 的第一位来说，他的sub array 的pre sum 是0
所以我们遍历数组每一个 j， 在 deque中从小到达寻找 有没有一个这样的sub array。
为什么我们一旦满足条件就需要pop出array 的第一位呢， 因为对于 之后的j 再次满足条件时，新的j 肯定比之前第一次满足条件的j 长度长，我们希望
j 尽可能的小，这样求出来的才是shortest sub array

'''