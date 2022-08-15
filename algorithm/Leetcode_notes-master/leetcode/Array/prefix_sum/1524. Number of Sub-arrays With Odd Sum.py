class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr:
            return 0
        odd = 0
        # 初始化， presum是0，所以前面有一个为even 的情况，防止[1]特殊case
        even = 1
        presum = 0
        result = 0
        for i in range(len(arr)):
            # 当前的sums 和
            presum += arr[i]
            # 如果当前sums 和 是偶数的话
            # 奇数 + 奇数 = 偶数
            # 那么只需要找到在当前array 中，有几个presum 为 奇数的数组，那么 肯定也有相对应奇数数组，后半部分肯定也是奇数
            if presum % 2 == 0:
                result += odd
                even += 1
            # 如果sums 为奇数的话’
            # 偶数 + 奇数 = 奇数
            # 找到当前array的presum 中，有几个为偶数的情况，那么也会有相对应的奇数 数组作为后半部分
            # 因为一个sums数组 会被分成两个部分，如果前半部分偶数数组存在，那么后半部分奇数数组肯定也存在
            else:
                result += even
                odd += 1
        return result % (10 ** 9 + 7)
