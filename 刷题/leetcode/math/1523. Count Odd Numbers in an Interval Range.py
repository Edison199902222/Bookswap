class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # 如果从奇数 到 偶数之间的odd 的话， 一定是对半分的
        # high + 1//2 代表 从1 到high之间有几个odd 数
        # low // 2 代表，1 到low - 1 之间有几个odd
        # 因为是整除，所以 high + 1 跟 high 无论high 是奇数还是偶数，得到的odd都是一样的
        # low 也是，无论low 是奇还是偶，得到的都是从1～low - 1的odd数量
        return (high + 1) // 2 - (low) // 2