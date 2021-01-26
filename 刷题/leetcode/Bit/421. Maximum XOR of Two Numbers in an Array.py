class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # a ^ b = c  -> a ^ c = b
        # 假设能求出现在c = max 假设 a ^ b = max， a 和 b 两个数 异或变成max的话
        # 那么 a 如果 跟 max 异或 那么b 也必将在数组中
        # 所以，我们一位一位假设max 值，然后跟nums 中每一位进行异或，也就把nums中每一个位都想象成a
        # 如果 a 跟 max 异或的结果 b 存在于nums中，那么 我们就可以得出当前的max是成立的

        max_number = 0
        bit_mask = 0
        # 求出最大值的二进制位数，-2是因为 py 有0b
        # 然后从最高位开始假设最大值
        length = len(bin(max(nums))) - 2
        for i in range(length, -1, -1):
            # 利用bitmask 得到每个数前缀，bitmask 永远都是 1100，1110， 这样可以得到前两位，两三位的前缀
            bit_mask |= (1 << i)
            hash_set = set()
            # 得到前缀
            for num in nums:
                hash_set.add(bit_mask & num)
            # 贪心，试着加上一个1
            cur_max = max_number | (1 << i)
            # 如果存在一个b， 那么把当前最大值赋给全局最大
            for num in hash_set:
                if num ^ cur_max in hash_set:
                    max_number = cur_max
                    break
        return max_number