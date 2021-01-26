class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        # 维护一个区间
        # lower， below
        # lower 是前一个数字的 + 1， below 是当前数字的 - 1
        # 比较两个大小关系，如果 lower 大于 below 说明中间没有数字
        # 如果 lower == below，说明有一个数字，就是 lower 或者 below
        # 如果lower 小于below， 说明有超过一个数字
        # 每次更新lower，记得结尾后还要检查一次 目的是检查最后一个跟upper
        result = []
        for num in nums:
            # below 代表 num 之前miss 的数
            below = num - 1
            if lower == below:
                result.append(str(lower))
            elif lower < below:
                result.append(str(lower) + "->" + str(below))
            # lower 代表 前一个数 后面会 miss的数
            lower = num + 1
        if lower == upper:
            result.append(str(lower))
        elif lower < upper:
            result.append(str(lower) + "->" + str(upper))
        return result
'''
可以把nums里的数看成是障碍物，其实是求两障碍物之间的区间。为了保证所求区间在[lower,upper]之间，
可以在lower-1和upper+1的位置上各放一个障碍物。从第一个障碍物起，每次碰到新的障碍物的时候去跟之前的障碍物的位置比较：
1）若前一障碍物的位置是当前障碍物位置-2，那么这两个障碍物之间只有有一个数；
2）若前一障碍物的位置<当前障碍物位置-2，那么这两个障碍物之间只有若干(>2)个数；
3）若前一障碍物的位置是当前障碍物位置-1，也就是不满足1）和2），那么继续下一个障碍物；
'''


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if not nums:
            if lower == upper:
                return [str(lower)]
            else:
                return [str(lower) + "->" + str(upper)]
        result = []
        for i in range(len(nums)):
            if i == 0:
                if abs(nums[i] - lower) >= 2:
                    result.append(str(lower) + "->" + str(nums[i] - 1))
                elif abs(nums[i] - lower) == 1:
                    result.append(str(lower))

            else:
                if abs(nums[i] - nums[i - 1]) == 2:
                    result.append(str(nums[i - 1] + 1))
                elif abs(nums[i] - nums[i - 1]) > 2:
                    result.append(str(nums[i - 1] + 1) + "->" + str(nums[i] - 1))
            if i == len(nums) - 1:
                if abs(upper - nums[i]) >= 2:
                    result.append(str(nums[i] + 1) + "->" + str(upper))
                elif abs(upper - nums[i]) == 1:
                    result.append(str(upper))
        return result