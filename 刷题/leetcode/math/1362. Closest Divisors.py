class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        # 思路： 乘集的最大值就是根号 + 1
        # 假设ab = num + 1/ ab = num + 2， 那么我们 枚举a
        # 已知 num + 1/ num + 2，a 我们求b，只需要 判断 如果num + 1/ num+2 除 a 没有余数
        # 那么说明有一组数a b 出现
        # 感觉思路有点像two sum
        result = []
        difference = float("inf")
        for i in range(int((num + 2)**0.5) + 1, 0, -1):
            if (num + 1) % i == 0:
                a = i
                b = (num + 1) // a
                if abs(a - b) < difference:
                    difference = abs(a - b)
                    result = [a, b]
            if (num + 2) % i == 0:
                a = i
                b = (num + 2) // a
                if abs(a - b) < difference:
                    difference = abs(a - b)
                    result = [a, b]
        return result