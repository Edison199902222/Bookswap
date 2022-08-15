class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        # 核心思想：看出规律，用right 表示当前最右边亮的灯泡
        # count 记录 当前有几个灯泡亮
        # 如果count 等于 right，说明在right 区间内，全部都亮了，那么说明moment + 1
        # right 维护一个区间
        result = 0
        count = 0
        right = 0
        for i in range(len(light)):
            count += 1
            right = max(right, light[i])
            if count == right:
                result += 1
        return result
