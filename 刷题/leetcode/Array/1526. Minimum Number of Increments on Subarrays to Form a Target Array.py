class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # 初始化result成第一位数，防止 数组中全是一样的的数字的情况
        # 初始化一开始 至少要result 这么多次 把数组中全变成 target第一个数
        result = target[0]
        for i in range(1, len(target)):
            # 如果当前数比前一个数大， 说明至少要当前数 减去 前一个数 这么多次 operation 才可以让0 变成当前数，
            # 因为前面的result已经让可以让当前数从0变成跟前一个数相同的数
            if target[i] > target[i - 1]:
                result += target[i] - target[i - 1]
        return result