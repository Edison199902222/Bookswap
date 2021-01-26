class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        left = min(sweetness)
        right = sum(sweetness) // (K + 1)
        while left + 1 < right:
            mid = (left + right) // 2
            # 不足构成 k + 1块， sweetness 太大， 调小
            if self.caculate(sweetness, mid) < K + 1:
                right = mid
            # 构成k + 1块， 尝试sweetness 变大
            else:
                left = mid
        # 因为想求 maximum total sweetness of the piece， 所以先检查right
        if self.caculate(sweetness, right) == K + 1:
            return right
        return left

    # 用来记录当我分到的巧克力甜度为value的时候，切的总块数
    def caculate(self, nums, value):
        count = 0
        sums = 0
        for num in nums:
            sums += num
            # 少于value 不算一块
            if sums >= value:
                count += 1
                sums = 0
        return count
'''
为什么 < K + 1 不取等号？
题目要求取 maximum total sweetness of the piece， 取等号会把更大的sweetness 给去掉
'''