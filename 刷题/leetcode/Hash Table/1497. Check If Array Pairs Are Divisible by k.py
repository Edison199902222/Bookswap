class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        dic = collections.defaultdict(int)
        # 把每一个数跟k的余数记录下来
        for i in arr:
            dic[i % k] += 1

        for i in range(len(arr)):
            temp = arr[i] % k
            # 第一种余数的情况，如果刚好等于k的一半， 也需要找k的一般凑成k
            # 就看自己本身出现的次数 是不是2的倍数
            if temp * 2 == k:
                if dic[temp] % 2 != 0:
                    return False
            # 第二种情况，余数 = 0
            elif temp == 0:
                if dic[temp] % 2 != 0:
                    return False
            # 第三种情况，想要凑成k的两个值的余数不等
            else:
                if dic[k - temp] != dic[temp]:
                    return False
        return True