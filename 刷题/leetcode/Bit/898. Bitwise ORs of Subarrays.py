class Solution(object):
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # cur 表示的是i - 1 的 异或的所有结果 subarray
        # 每次拿上一层的每一个结果，跟当前第i 个元素进行异或 放进temp中
        # 结束后，把cur = temp 因为temp是这一层的结果，再加上 i， 因为i 自己也是一个subarray
        res, cur = set(), set()
        for i in A:
            temp = set()
            # 计算当前层的所有subarray 异或结果
            for j in cur:
                temp.add(j | i)
            cur = temp
            # 加上当前元素
            cur |= {i}
            res |= cur
        return len(res)