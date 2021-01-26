class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bitmask = 0
        for num in nums:
            # 找出出现一次的两个element的difference
            bitmask ^= num
        # 找到difference 最右边为1的那一位
        # 因为 可以根据最右边那一位来判断 x 跟 y
        diff = bitmask & (-bitmask)
        num1= 0
        num2 = 0
        for num in nums:
            # 如果difference 跟当前数字 的 & 为1，说明这可能是第一个数字
            if diff & num:
                num1 ^= num
            # 如果为0，可能是第二个数字
            else:
                num2 ^= num
        #为什么把所有的元素都重新异或了？其实，因为除了这两个元素以外，其他的元素都出现了两次，这两次相同的数字的和               # mask的与操作的结果是相同的，所以会被异或两次抵消掉
        return [num1, num2]