class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        prefix_sum = 0
        # 整个nums 除于 p， 要寻找一个subarray 的余数 跟 rest 相等，这样 整个大区间 减去rest 小subarray，剩下的就是余数为0
        rest = sum(nums) % p
        if rest == 0:
            return 0
        # 初始化,记录每个区间的余数
        dic = {0: -1}
        n = len(nums)
        result = n
        for i in range(len(nums)):
            prefix_sum += nums[i]
            # 记录当前区间余几
            cur = prefix_sum % p
            # 用当前区间余了几表示 0 到 j 区间 的余数，减去需要rest 余数 表示 i 到j 区间需要rest的余数 = 0 到 i 区间我们需要几的余数
            # 0 。。。i。。。j。。。end   意思是假设 rest = 3， 我们需要余数为3 的subarray， 然后现在0 到 j 的余数 cur = 5
            # 用cur - rest + p = 2 这样 可以知道 0...i 要多少的余数，才能使得i .. j 余数是3， 这个例子 0..i余数是2 就可以使得i到j余数是3
            # 这样就符合土木要求了， 加p是怕为负数，加上p 除余p reminder 不变
            x = (cur - rest + p) % p
            if x in dic:
                result = min(result, i - dic[x])
            dic[cur] = i
        return result if result != n else - 1
